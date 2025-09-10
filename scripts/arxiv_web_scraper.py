#!/usr/bin/env python3
"""
arXiv 网页爬虫模块 - 直接从 arXiv 网页爬取论文信息
替代 arxiv 库的功能
"""

import requests
import re
from bs4 import BeautifulSoup
from typing import List, Dict, Any, Optional    
from urllib.parse import urljoin
import datetime
from dataclasses import dataclass

@dataclass
class Paper:
    """论文数据类，模拟 arxiv 库的 Result 对象结构"""
    entry_id: str
    title: str
    authors: List[Dict[str, str]]  # [{"name": "Author Name"}, ...]
    summary: str
    pdf_url: str
    published: Optional[datetime.datetime] = None
    updated: Optional[datetime.datetime] = None
    categories: List[str] = None
    primary_category: str = ""

    def __post_init__(self):
        if self.categories is None:
            self.categories = []

class ArxivWebScraper:
    """arXiv 网页爬虫类"""
    
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })
        self.base_url = "https://arxiv.org"
    
    def fetch_category_new(self, category: str) -> tuple[List[Paper], dict]:
        """
        获取特定类别的新论文 (New submissions)
        Args:
            category: 类别名称，如 'gr-qc', 'astro-ph.CO' 等
        Returns:
            tuple[List[Paper], dict]: (论文列表, 统计信息)
        """
        url = f"{self.base_url}/list/{category}/new"
        print(f"🔍 正在爬取 {url}")
        
        stats = {
            "category": category,
            "url": url,
            "expected_total": 0,
            "actual_crawled": 0,
            "page_source_info": "",
            "success": False,
            "verification_passed": False
        }
        
        try:
            response = self.session.get(url, timeout=30)
            response.raise_for_status()
            response.encoding = 'utf-8'
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # 提取页面总数信息并进行自检
            expected_total, page_info = self._extract_total_count(soup)
            stats["expected_total"] = expected_total
            stats["page_source_info"] = page_info
            
            # 解析论文
            papers = self._parse_arxiv_list_page(soup)
            stats["actual_crawled"] = len(papers)
            stats["success"] = True
            
            # 验证爬取数量是否匹配
            if expected_total > 0:
                # 允许一定的容错范围（±5篇）
                tolerance = 5
                if abs(expected_total - len(papers)) <= tolerance:
                    stats["verification_passed"] = True
                    print(f"✅ 验证通过: 页面显示 {expected_total} 篇，实际爬取 {len(papers)} 篇")
                else:
                    stats["verification_passed"] = False
                    print(f"⚠️ 数量不匹配: 页面显示 {expected_total} 篇，实际爬取 {len(papers)} 篇")
            else:
                print(f"⚠️ 无法获取页面总数，实际爬取 {len(papers)} 篇")
            
            return papers, stats
            
        except requests.RequestException as e:
            print(f"❌ 爬取 {category} 失败: {e}")
            stats["error"] = str(e)
            return [], stats
    
    def fetch_category_recent(self, category: str, days: int = 5) -> tuple[List[Paper], dict]:
        """
        获取特定类别的最近论文 (Recent submissions, Cross-lists, Replacements)
        """
        url = f"{self.base_url}/list/{category}/recent"
        print(f"🔍 正在爬取最近论文 {url}")
        
        stats = {
            "category": category,
            "url": url,
            "expected_total": 0,
            "actual_crawled": 0,
            "page_source_info": "Recent submissions page",
            "success": False,
            "verification_passed": True  # Recent 页面通常不显示总数
        }
        
        try:
            response = self.session.get(url, timeout=30)
            response.raise_for_status()
            response.encoding = 'utf-8'
            
            soup = BeautifulSoup(response.text, 'html.parser')
            papers = self._parse_arxiv_list_page(soup)
            
            stats["actual_crawled"] = len(papers)
            stats["success"] = True
            
            return papers, stats
            
        except requests.RequestException as e:
            print(f"❌ 爬取 {category} 最近论文失败: {e}")
            stats["error"] = str(e)
            return [], stats
    
    def _extract_total_count(self, soup: BeautifulSoup) -> tuple[int, str]:
        """
        提取页面总数信息并进行自检
        Returns:
            tuple[int, str]: (总数, 原始文本)
        """
        total_count = 0
        original_text = ""
        
        # 方法1: 查找 paging div 中的信息
        paging_div = soup.find('div', class_='paging')
        if paging_div:
            text = paging_div.get_text()
            match = re.search(r'Total of (\d+) entries', text)
            if match:
                total_count = int(match.group(1))
                original_text = text.strip()
                print(f"📊 在 paging div 中找到总数: {total_count}")
                return total_count, original_text
        
        # 方法2: 查找包含 "Total of X entries" 的任何文本
        total_pattern = re.compile(r'Total of (\d+) entries', re.IGNORECASE)
        for element in soup.find_all(string=total_pattern):
            match = total_pattern.search(element)
            if match:
                total_count = int(match.group(1))
                original_text = element.strip()
                print(f"📊 在文本中找到总数: {total_count}")
                return total_count, original_text
        
        # 方法3: 查找任何包含数字和 entries 的文本
        for text in soup.find_all(string=True):
            if 'entries' in text.lower() and re.search(r'\d+', text):
                numbers = re.findall(r'\d+', text)
                if numbers:
                    total_count = int(numbers[0])  # 取第一个数字
                    original_text = text.strip()
                    print(f"📊 通过模糊匹配找到总数: {total_count}")
                    return total_count, original_text
        
        print("⚠️ 未找到页面总数信息")
        return 0, "未找到总数信息"
    
    def _parse_arxiv_list_page(self, soup: BeautifulSoup) -> List[Paper]:
        """解析 arXiv 列表页面"""
        papers = []
        
        # 查找所有论文条目 - arXiv 使用 <dt> 和 <dd> 标签对
        dt_elements = soup.find_all('dt')
        dd_elements = soup.find_all('dd')
        
        print(f"🔍 找到 {len(dt_elements)} 个 <dt> 元素，{len(dd_elements)} 个 <dd> 元素")
        
        # 确保 dt 和 dd 数量匹配
        min_count = min(len(dt_elements), len(dd_elements))
        
        for i in range(min_count):
            try:
                dt = dt_elements[i]
                dd = dd_elements[i]
                
                paper = self._parse_paper_entry(dt, dd)
                if paper:
                    papers.append(paper)
                    
            except Exception as e:
                print(f"⚠️ 解析论文条目 {i+1} 失败: {e}")
                continue
        
        print(f"✅ 成功解析 {len(papers)} 篇论文")
        return papers
    
    def _parse_paper_entry(self, dt_element, dd_element) -> Optional[Paper]:
        """解析单个论文条目"""
        try:
            # 从 dt 元素提取 arXiv ID 和提交类型信息
            arxiv_id, submission_info = self._extract_arxiv_id(dt_element)
            if not arxiv_id:
                return None
            
            # 从 dd 元素提取详细信息
            title = self._extract_title(dd_element)
            authors = self._extract_authors(dd_element)
            summary = self._extract_summary(dd_element)
            categories, primary_category = self._extract_categories(dd_element)
            dates = self._extract_dates(dd_element)
            
            # 构建 PDF URL
            pdf_url = f"{self.base_url}/pdf/{arxiv_id}.pdf"
            entry_id = f"{self.base_url}/abs/{arxiv_id}"
            
            # 创建论文对象
            paper = Paper(
                entry_id=entry_id,
                title=title,
                authors=authors,
                summary=summary,
                pdf_url=pdf_url,
                published=dates.get('published'),
                updated=dates.get('updated'),
                categories=categories,
                primary_category=primary_category
            )
            
            # 添加提交类型信息作为属性
            paper.submission_info = submission_info
            
            return paper
            
        except Exception as e:
            print(f"⚠️ 解析论文详情失败: {e}")
            return None
    
    def _extract_arxiv_id(self, dt_element) -> tuple[Optional[str], dict]:
        """
        提取 arXiv ID 和提交类型信息
        Returns:
            tuple[Optional[str], dict]: (arXiv_id, submission_info)
        """
        text = dt_element.get_text()
        submission_info = {"type": "new", "details": "", "cross_list_from": ""}
        
        # 使用正则表达式匹配 arXiv ID
        arxiv_pattern = r'arXiv:(\d{4}\.\d{4,5})'
        match = re.search(arxiv_pattern, text)
        
        arxiv_id = None
        if match:
            arxiv_id = match.group(1)
        else:
            # 备用方法：查找链接
            links = dt_element.find_all('a', href=True)
            for link in links:
                href = link['href']
                if '/abs/' in href:
                    arxiv_id = href.split('/abs/')[-1]
                    break
        
        # 解析提交类型信息
        if arxiv_id:
            # 检查是否是 replaced
            if '(replaced)' in text.lower():
                submission_info["type"] = "replaced"
                submission_info["details"] = "replaced"
            
            # 检查是否是 cross-list
            cross_list_match = re.search(r'\(cross-list from ([^)]+)\)', text, re.IGNORECASE)
            if cross_list_match:
                submission_info["type"] = "cross-list"
                submission_info["cross_list_from"] = cross_list_match.group(1)
                submission_info["details"] = f"cross-list from {cross_list_match.group(1)}"
            
            # 如果找不到特殊标记，默认为新提交
            if submission_info["type"] == "new" and submission_info["details"] == "":
                submission_info["details"] = "new submission"
        
        return arxiv_id, submission_info
    
    def _extract_title(self, dd_element) -> str:
        """提取标题"""
        # 查找 Title: 后面的内容
        title_div = dd_element.find('div', class_='list-title')
        if title_div:
            title_text = title_div.get_text()
            # 移除 "Title: " 前缀
            title = re.sub(r'^Title:\s*', '', title_text, flags=re.IGNORECASE).strip()
            return title
        
        # 备用方法：直接从文本中提取
        text = dd_element.get_text()
        lines = text.split('\n')
        
        # 标题通常在第一行或第二行
        for line in lines[:3]:
            line = line.strip()
            if line and not line.startswith(('Authors:', 'Comments:', 'Subjects:', 'Journal-ref:')):
                # 移除可能的 "Title:" 前缀
                title = re.sub(r'^Title:\s*', '', line, flags=re.IGNORECASE).strip()
                if title and len(title) > 10:  # 确保是有意义的标题
                    return title
        
        return "未找到标题"
    
    def _extract_authors(self, dd_element) -> List[Dict[str, str]]:
        """提取作者列表"""
        # 查找作者信息
        text = dd_element.get_text()
        
        # 使用正则表达式查找作者部分
        # arXiv 格式通常是：Title\n作者名单\nComments: ... 或 Subjects: ...
        lines = text.split('\n')
        
        authors_line = ""
        for i, line in enumerate(lines):
            line = line.strip()
            if line and not line.startswith(('Title:', 'Comments:', 'Subjects:', 'Journal-ref:')):
                # 如果这不是第一行（标题），可能是作者行
                if i > 0:
                    # 检查下一行是否是 Comments 或 Subjects，如果是，当前行可能是作者
                    next_line = lines[i+1].strip() if i+1 < len(lines) else ""
                    if next_line.startswith(('Comments:', 'Subjects:', 'Journal-ref:')) or i == len(lines) - 1:
                        authors_line = line
                        break
        
        # 解析作者名单
        authors = []
        if authors_line:
            # 清理作者行，移除机构信息（通常在括号内）
            # 但保留基本的姓名信息
            authors_clean = re.sub(r'\([^)]*\)', '', authors_line)  # 移除括号内容
            
            # 分割作者名字 - 通常以逗号分隔
            author_names = re.split(r',\s*(?![^(]*\))', authors_clean)  # 不在括号内的逗号
            
            for name in author_names:
                name = name.strip()
                if name and len(name) > 1:  # 过滤掉单字符
                    # 进一步清理名字
                    name = re.sub(r'^\d+\.\s*', '', name)  # 移除编号
                    name = re.sub(r'\s+', ' ', name)  # 规范化空格
                    if name and len(name) > 2:
                        authors.append({"name": name})
        
        # 如果没找到作者，尝试另一种方法
        if not authors:
            # 查找包含人名模式的行
            for line in lines:
                line = line.strip()
                # 简单的人名模式匹配（包含大写字母开头的单词）
                if re.search(r'^[A-Z][a-z]+\s+[A-Z]', line) and not line.startswith(('Title:', 'Comments:', 'Subjects:')):
                    authors = [{"name": line}]
                    break
        
        return authors if authors else [{"name": "Unknown Author"}]
    
    def _extract_summary(self, dd_element) -> str:
        """提取摘要"""
        text = dd_element.get_text()
        lines = text.split('\n')
        
        # 摘要通常是最后的一大段文本，不包含特定的前缀
        summary_lines = []
        in_summary = False
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
                
            # 跳过标题、作者、评论、学科等元数据
            if line.startswith(('Title:', 'Authors:', 'Comments:', 'Subjects:', 'Journal-ref:', 'DOI:', 'Report-no:')):
                in_summary = False
                continue
            
            # 如果是元数据行之后的内容，可能是摘要
            if not in_summary and line and len(line) > 30:  # 假设摘要行比较长
                in_summary = True
            
            if in_summary:
                summary_lines.append(line)
        
        summary = ' '.join(summary_lines).strip()
        
        # 如果没找到明显的摘要，使用备用方法
        if not summary or len(summary) < 50:
            # 查找最长的文本段落
            max_line = ""
            for line in lines:
                line = line.strip()
                if len(line) > len(max_line) and not line.startswith(('Title:', 'Authors:', 'Comments:', 'Subjects:', 'Journal-ref:')):
                    max_line = line
            summary = max_line
        
        return summary if summary else "未找到摘要"
    
    def _extract_categories(self, dd_element) -> tuple[List[str], str]:
        """提取类别信息"""
        text = dd_element.get_text()
        
        # 查找 Subjects: 行
        subjects_match = re.search(r'Subjects:\s*(.+?)(?:\n|$)', text, re.IGNORECASE)
        if not subjects_match:
            return [], ""
        
        subjects_text = subjects_match.group(1).strip()
        
        # 解析类别
        categories = []
        primary_category = ""
        
        # 清理 HTML 标签（如果有）
        subjects_clean = re.sub(r'<[^>]+>', '', subjects_text)
        
        # 分割类别 - 通常以分号或逗号分隔
        parts = re.split(r'[;,]\s*', subjects_clean)
        
        for part in parts:
            part = part.strip()
            if not part:
                continue
                
            # 提取类别代码
            # 查找模式如 "General Relativity and Quantum Cosmology (gr-qc)"
            cat_match = re.search(r'\(([a-z-]+(?:\.[A-Z]{2})?)\)', part)
            if cat_match:
                cat_code = cat_match.group(1)
                categories.append(cat_code)
                if not primary_category:
                    primary_category = cat_code
            else:
                # 如果没有括号，尝试直接匹配类别代码
                direct_match = re.search(r'^([a-z-]+(?:\.[A-Z]{2})?)(?:\s|$)', part)
                if direct_match:
                    cat_code = direct_match.group(1)
                    categories.append(cat_code)
                    if not primary_category:
                        primary_category = cat_code
        
        return categories, primary_category
    
    def _extract_dates(self, dd_element) -> Dict[str, Optional[datetime.datetime]]:
        """提取发布和更新日期"""
        dates = {"published": None, "updated": None}
        
        text = dd_element.get_text()
        
        # 查找提交日期 - 多种可能的格式
        date_patterns = [
            r'Submitted on\s+(\d{1,2}\s+\w{3}\s+\d{4})',
            r'submitted\s+(\d{1,2}\s+\w{3}\s+\d{4})',
            r'\[(\d{1,2}\s+\w{3}\s+\d{4})\]',
            r'(\d{1,2}\s+\w{3}\s+\d{4})'  # 直接的日期格式
        ]
        
        for pattern in date_patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                try:
                    date_str = match.group(1)
                    dates["published"] = datetime.datetime.strptime(date_str, "%d %b %Y")
                    break
                except ValueError:
                    continue
        
        # 如果没有找到明确日期，使用今天作为默认值
        if not dates["published"]:
            dates["published"] = datetime.datetime.now()
        
        return dates

# 向后兼容性：创建与 arxiv 库类似的接口
class Client:
    """模拟 arxiv.Client 的接口"""
    
    def __init__(self):
        self.scraper = ArxivWebScraper()
    
    def results(self, search) -> List[Paper]:
        """模拟 arxiv 库的 results 方法"""
        return search.execute(self.scraper)

class Search:
    """模拟 arxiv.Search 的接口"""
    
    def __init__(self, query: str, max_results: int = 10, **kwargs):
        self.query = query
        self.max_results = max_results
        self.sort_by = kwargs.get('sort_by')
        self.sort_order = kwargs.get('sort_order')
    
    def execute(self, scraper: ArxivWebScraper) -> List[Paper]:
        """执行搜索"""
        papers = []
        all_stats = []
        
        # 解析查询字符串，提取类别
        categories = self._parse_query_categories()
        
        for category in categories:
            # 获取新论文
            new_papers, new_stats = scraper.fetch_category_new(category)
            papers.extend(new_papers)
            all_stats.append(new_stats)
            
            # 如果需要更多结果，也获取最近论文
            if len(papers) < self.max_results:
                recent_papers, recent_stats = scraper.fetch_category_recent(category)
                papers.extend(recent_papers)
                all_stats.append(recent_stats)
        
        # 去重（基于 entry_id）
        unique_papers = {}
        for paper in papers:
            paper_id = paper.entry_id.split('/')[-1]
            if paper_id not in unique_papers:
                unique_papers[paper_id] = paper
        
        papers = list(unique_papers.values())
        
        # 限制结果数量
        if len(papers) > self.max_results:
            papers = papers[:self.max_results]
        
        # 存储统计信息供后续使用
        if hasattr(scraper, 'last_stats'):
            scraper.last_stats = all_stats
        
        return papers
    
    def _parse_query_categories(self) -> List[str]:
        """解析查询字符串中的类别"""
        categories = []
        
        # 匹配 cat:category 格式
        cat_matches = re.findall(r'cat:([a-z-]+(?:\.[A-Z]{2})?(?:\.\*)?)', self.query)
        
        for match in cat_matches:
            if match.endswith('.*'):
                # 处理通配符，如 astro-ph.*
                base_cat = match[:-2]  # 移除 .*
                if base_cat == 'astro-ph':
                    # 添加所有 astro-ph 子类别
                    categories.extend([
                        'astro-ph.CO',  # 宇宙学
                        'astro-ph.HE',  # 高能天体物理
                        'astro-ph.GA',  # 银河系天体物理
                        'astro-ph.SR',  # 恒星物理
                        'astro-ph.IM',  # 仪器和方法
                        'astro-ph.EP'   # 地外行星
                    ])
                else:
                    categories.append(base_cat)
            else:
                categories.append(match)
        
        # 如果没有找到类别，默认使用 gr-qc
        if not categories:
            categories = ['gr-qc']
        
        return categories

# 兼容性枚举类
class SortCriterion:
    SubmittedDate = "submittedDate"
    LastUpdatedDate = "lastUpdatedDate"
    Relevance = "relevance"

class SortOrder:
    Ascending = "ascending" 
    Descending = "descending"

# 导出接口，保持与 arxiv 库的兼容性
__all__ = ['Client', 'Search', 'Paper', 'SortCriterion', 'SortOrder', 'ArxivWebScraper']
