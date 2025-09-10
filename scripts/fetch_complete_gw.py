#!/usr/bin/env python3
"""
完整引力波论文爬取脚本 - 分别爬取 GR-QC 和 Astro-Ph 确保获取完整数据
使用网页爬虫代替 arxiv 库
"""

# 使用本地的网页爬虫模块代替 arxiv 库
from arxiv_web_scraper import Client, Search, SortCriterion, SortOrder
import datetime
import os
import json
from pathlib import Path
from typing import List, Any

# 尝试加载 .env 文件
try:
    from dotenv import load_dotenv
    load_dotenv()
    print("✅ 已加载 .env 文件")
except ImportError:
    print("⚠️ python-dotenv 未安装，使用系统环境变量")

# 配置
ARXIV_MAX_RESULTS = int(os.getenv('ARXIV_MAX_RESULTS', '300'))
ARCHIVE_DIR = os.getenv('ARCHIVE_DIR', 'archives/complete')
ENABLE_ARCHIVE = os.getenv('ENABLE_ARCHIVE', 'true').lower() == 'true'
MATTERMOST_WEBHOOK_URL = os.getenv('MATTERMOST_WEBHOOK_URL')
MATTERMOST_MAX_PAPERS = int(os.getenv('MATTERMOST_MAX_PAPERS', '20'))

def fetch_category_papers(category: str, max_results: int = 200):
    """获取特定类别的论文，包含自检功能"""
    print(f"📡 正在获取 {category} 类别的文章...")
    
    from arxiv_web_scraper import ArxivWebScraper
    scraper = ArxivWebScraper()
    
    # 直接获取新论文和统计信息
    papers, stats = scraper.fetch_category_new(category)
    
    print(f"✅ {category}: 获取到 {len(papers)} 篇文章")
    
    # 显示验证结果
    if stats.get("verification_passed"):
        print(f"   ✅ 自检通过: 页面显示 {stats['expected_total']} 篇，实际爬取 {stats['actual_crawled']} 篇")
    elif stats.get("expected_total", 0) > 0:
        print(f"   ⚠️ 自检异常: 页面显示 {stats['expected_total']} 篇，实际爬取 {stats['actual_crawled']} 篇")
    else:
        print(f"   ⚠️ 无法获取页面总数进行验证")
    
    return papers, stats

def filter_today_papers(papers):
    """筛选今天的文章（包括 New submissions, Cross-lists, Replacements）"""
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1)
    recent_dates = [today, yesterday]  # 包括昨天以捕获跨时区的文章
    
    today_papers = []
    
    for paper in papers:
        if paper.published:
            pub_date = paper.published.date()
            upd_date = paper.updated.date() if paper.updated else pub_date
            
            # 如果发布日期或更新日期在最近范围内
            if pub_date in recent_dates or upd_date in recent_dates:
                today_papers.append(paper)
    
    return today_papers

def filter_gravitational_wave_papers(papers):
    """筛选引力波相关论文"""
    filtered_papers = []
    
    for paper in papers:
        title_text = paper.title.lower()
        abstract_text = paper.summary.lower()
        
        # 首先检查是否包含 "wave"
        if 'wave' in title_text or 'wave' in abstract_text:
            combined_text = f"{title_text} {abstract_text}"
            
            # 检查是否为引力波相关
            gw_patterns = [
                'gravitational wave', 'gravitational waves', 'gravitational-wave', 'gravitational-waves',
                ' gw ', 'ligo', 'virgo', 'kagra', 'lisa', 'taiji', 'tianqin',
                'einstein telescope', 'cosmic explorer'
            ]
            
            if any(pattern in combined_text for pattern in gw_patterns):
                filtered_papers.append(paper)
    
    return filtered_papers

def classify_submission_type(paper) -> str:
    """分类提交类型"""
    primary_cat = paper.primary_category
    all_categories = paper.categories
    published = paper.published
    updated = paper.updated
    
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1)
    recent_dates = [today, yesterday]
    
    if published and updated:
        pub_date = published.date()
        upd_date = updated.date()
        
        # Replacement: 更新日期在最近，但发布日期不是
        if upd_date in recent_dates and pub_date not in recent_dates:
            return "Replacement"
        
        # Cross-list: 主类别不是目标类别，但包含目标类别
        target_categories = ['gr-qc', 'astro-ph.CO', 'astro-ph.HE', 'astro-ph.IM', 'astro-ph.GA', 'astro-ph.SR', 'astro-ph.EP']
        
        if primary_cat not in target_categories:
            for cat in all_categories:
                if cat in target_categories:
                    return "Cross-list"
        
        # New: 发布日期在最近
        if pub_date in recent_dates:
            return "New"
    
    return "New"

def format_mattermost_message(papers: List[Any], date_str: str) -> str:
    """格式化 Mattermost 消息 - 严格按照提供的格式"""
    
    message_parts = []
    
    # 标题
    total_papers = len(papers)
    message_parts.append(f"# 📡 Daily GW arXiv Digest - {date_str}")
    message_parts.append(f"**Found {total_papers} gravitational wave papers**")
    message_parts.append("")
    
    # 显示论文，严格按照格式，包含提交类型信息
    for paper in papers[:MATTERMOST_MAX_PAPERS]:
        # arXiv ID
        arxiv_id = paper.entry_id.split('/')[-1]
        
        # 发布日期
        pub_date = paper.published.strftime('%d %b %Y') if paper.published else 'Unknown date'
        
        # 作者列表
        authors = [author["name"] for author in paper.authors]
        author_str = ', '.join(authors)
        
        # 类别信息
        primary_cat = paper.primary_category
        other_cats = [cat for cat in paper.categories if cat != primary_cat]
        
        # 构建提交信息 - 根据提交类型添加标记
        submission_info = getattr(paper, 'submission_info', {})
        submission_type = submission_info.get('type', 'new')
        
        if submission_type == 'replaced':
            arxiv_link = f"[arXiv:{arxiv_id}](https://arxiv.org/abs/{arxiv_id}) (replaced) [Submitted on {pub_date}]"
        elif submission_type == 'cross-list':
            cross_list_from = submission_info.get('cross_list_from', 'unknown')
            arxiv_link = f"[arXiv:{arxiv_id}](https://arxiv.org/abs/{arxiv_id}) (cross-list from {cross_list_from}) [Submitted on {pub_date}]"
        else:
            arxiv_link = f"[arXiv:{arxiv_id}](https://arxiv.org/abs/{arxiv_id})[Submitted on {pub_date}]"
        
        # 按照格式输出
        message_parts.append(arxiv_link)
        message_parts.append(f"**{paper.title}**")
        message_parts.append(f"{author_str}")
        
        if other_cats:
            subjects_str = f"**{primary_cat}**; {', '.join(other_cats)}"
        else:
            subjects_str = f"**{primary_cat}**"
        message_parts.append(f"Subjects: {subjects_str}")
        
        # 分割线
        message_parts.append("")
        message_parts.append("---")
        message_parts.append("")
    
    # 统计提交类型信息（基于网页源代码解析）
    submission_stats = {"new": 0, "cross-list": 0, "replaced": 0}
    for paper in papers:
        submission_info = getattr(paper, 'submission_info', {})
        submission_type = submission_info.get('type', 'new')
        submission_stats[submission_type] = submission_stats.get(submission_type, 0) + 1
    
    message_parts.append(f"📊 **Summary**: {submission_stats.get('new', 0)} New • {submission_stats.get('cross-list', 0)} Cross-lists • {submission_stats.get('replaced', 0)} Replacements")
    
    if len(papers) > MATTERMOST_MAX_PAPERS:
        message_parts.append(f"📋 Showing top {MATTERMOST_MAX_PAPERS} of {len(papers)} papers")
    
    return "\n".join(message_parts)

def save_to_archive(all_papers, gw_papers, date_str, crawl_stats=None):
    """保存文章到存档文件，支持按类别分类"""
    if not ENABLE_ARCHIVE:
        return
    
    # 确保存档目录结构存在
    archive_path = Path(ARCHIVE_DIR)
    archive_path.mkdir(parents=True, exist_ok=True)
    
    # 确保 archives 根目录和子目录都存在
    archives_root = Path('archives')
    archives_root.mkdir(exist_ok=True)
    
    complete_dir = archives_root / 'complete'
    filtered_dir = archives_root / 'filtered'
    
    complete_dir.mkdir(exist_ok=True)
    filtered_dir.mkdir(exist_ok=True)
    
    print(f"📁 确保存档目录结构存在: {archives_root.absolute()}")
    
    # 按类别分组论文
    gr_qc_papers = [p for p in all_papers if p.primary_category == 'gr-qc']
    astro_ph_papers = [p for p in all_papers if p.primary_category.startswith('astro-ph')]
    gw_gr_qc = [p for p in gw_papers if p.primary_category == 'gr-qc']
    gw_astro = [p for p in gw_papers if p.primary_category.startswith('astro-ph')]
    
    # 1. 保存筛选后的引力波论文存档 - 保存到 filtered 目录
    gw_filtered_file = filtered_dir / f"gw_filtered_{date_str}.json"
    
    gw_filtered_data = {
        "date": date_str,
        "crawl_timestamp": datetime.datetime.now().isoformat(),
        "query": "cat:gr-qc OR cat:astro-ph.* (filtered for gravitational waves)",
        "summary": {
            "total_crawled": len(all_papers),
            "total_gw_papers": len(gw_papers),
            "by_category": {
                "gr-qc": {
                    "total": len(gr_qc_papers),
                    "gw_related": len(gw_gr_qc)
                },
                "astro-ph": {
                    "total": len(astro_ph_papers), 
                    "gw_related": len(gw_astro)
                }
            }
        },
        "crawl_verification": crawl_stats or {},
        "papers": []
    }
    
    for paper in gw_papers:
        # 提取提交类型信息（从dt元素解析）
        submission_info = getattr(paper, 'submission_info', {})
        
        paper_data = {
            "id": paper.entry_id,
            "title": paper.title,
            "authors": [author["name"] for author in paper.authors],
            "abstract": paper.summary,
            "pdf_url": paper.pdf_url,
            "published": paper.published.isoformat() if paper.published else None,
            "updated": paper.updated.isoformat() if paper.updated else None,
            "categories": paper.categories,
            "primary_category": paper.primary_category,
            "submission_info": submission_info  # 新增：提交类型信息
        }
        gw_filtered_data["papers"].append(paper_data)
    
    with open(gw_filtered_file, 'w', encoding='utf-8') as f:
        json.dump(gw_filtered_data, f, ensure_ascii=False, indent=2)
    
    print(f"📁 引力波筛选存档已保存: {gw_filtered_file}")
    
    # 2. 按类别分别保存详细存档 - 确保在 complete 目录中
    # GR-QC 存档
    if gr_qc_papers:
        gr_qc_file = complete_dir / f"gr_qc_{date_str}.json"
        gr_qc_data = {
            "date": date_str,
            "category": "gr-qc",
            "url": "https://arxiv.org/list/gr-qc/new",
            "total_papers": len(gr_qc_papers),
            "gw_related_papers": len(gw_gr_qc),
            "papers": [
                {
                    "id": p.entry_id,
                    "title": p.title,
                    "authors": [a["name"] for a in p.authors],
                    "abstract": p.summary,
                    "pdf_url": p.pdf_url,
                    "categories": p.categories,
                    "is_gw_related": p in gw_papers
                }
                for p in gr_qc_papers
            ]
        }
        
        with open(gr_qc_file, 'w', encoding='utf-8') as f:
            json.dump(gr_qc_data, f, ensure_ascii=False, indent=2)
        
        print(f"📁 GR-QC 存档已保存: {gr_qc_file}")
    
    # Astro-Ph 存档
    if astro_ph_papers:
        astro_file = complete_dir / f"astro_ph_{date_str}.json"
        astro_data = {
            "date": date_str,
            "category": "astro-ph",
            "subcategories": list(set(p.primary_category for p in astro_ph_papers)),
            "total_papers": len(astro_ph_papers),
            "gw_related_papers": len(gw_astro),
            "papers": [
                {
                    "id": p.entry_id,
                    "title": p.title,
                    "authors": [a["name"] for a in p.authors],
                    "abstract": p.summary,
                    "pdf_url": p.pdf_url,
                    "categories": p.categories,
                    "primary_category": p.primary_category,
                    "is_gw_related": p in gw_papers
                }
                for p in astro_ph_papers
            ]
        }
        
        with open(astro_file, 'w', encoding='utf-8') as f:
            json.dump(astro_data, f, ensure_ascii=False, indent=2)
        
        print(f"📁 Astro-Ph 存档已保存: {astro_file}")
    
    print(f"✅ 存档完成: 筛选存档 + 分类存档 (总计 {len(gw_papers)} 篇引力波论文)")

def send_to_mattermost(message: str) -> bool:
    """发送消息到 Mattermost"""
    if not MATTERMOST_WEBHOOK_URL:
        print("⚠️ MATTERMOST_WEBHOOK_URL 未设置")
        return False
    
    import requests
    payload = {
        "text": message,
        "username": "GW arXiv Bot",
        "icon_emoji": ":telescope:"
    }
    
    try:
        response = requests.post(MATTERMOST_WEBHOOK_URL, json=payload, timeout=10)
        if response.status_code == 200:
            print("✅ 消息已发送到 Mattermost")
            return True
        else:
            print(f"❌ Mattermost 发送失败: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Mattermost 发送错误: {e}")
        return False

def main():
    """主函数 - 分别爬取 gr-qc 和 astro-ph 获取完整数据"""
    print("🔍 开始完整爬取 GR-QC 和 Astro-Ph 文章...")
    
    # 分别爬取每个类别以确保获取完整数据
    all_papers = []
    all_stats = []
    
    # 1. 爬取 gr-qc 类别
    print("\n=== 爬取 GR-QC 类别 ===")
    gr_qc_papers, gr_qc_stats = fetch_category_papers("gr-qc", 100)  # gr-qc 通常每天 ~50 篇
    all_papers.extend(gr_qc_papers)
    all_stats.append(gr_qc_stats)
    
    # 2. 爬取各个 astro-ph 子类别
    print("\n=== 爬取 Astro-Ph 子类别 ===")
    astro_categories = [
        "astro-ph.CO",  # 宇宙学
        "astro-ph.HE",  # 高能天体物理
        "astro-ph.GA",  # 银河系天体物理
        "astro-ph.SR",  # 恒星物理
        "astro-ph.IM",  # 仪器和方法
        "astro-ph.EP"   # 地外行星
    ]
    
    for category in astro_categories:
        cat_papers, cat_stats = fetch_category_papers(category, 50)  # 每个子类别最多 50 篇
        all_papers.extend(cat_papers)
        all_stats.append(cat_stats)
    
    print(f"\n📊 总共获取到 {len(all_papers)} 篇文章")
    
    # 去重（基于 arXiv ID）
    unique_papers = {}
    for paper in all_papers:
        paper_id = paper.entry_id.split('/')[-1]
        if paper_id not in unique_papers:
            unique_papers[paper_id] = paper
    
    all_papers = list(unique_papers.values())
    print(f"📊 去重后: {len(all_papers)} 篇文章")
    
    # 显示爬取验证总结
    print(f"\n=== 爬取验证总结 ===")
    total_expected = sum(s.get('expected_total', 0) for s in all_stats)
    total_actual = sum(s.get('actual_crawled', 0) for s in all_stats)
    verification_passed = all(s.get('verification_passed', False) for s in all_stats if s.get('expected_total', 0) > 0)
    
    print(f"📊 期望总数: {total_expected} 篇")
    print(f"📊 实际爬取: {total_actual} 篇")
    print(f"📊 验证状态: {'✅ 全部通过' if verification_passed else '⚠️ 部分异常'}")
    
    # 详细验证报告
    for stats in all_stats:
        category = stats.get('category', 'Unknown')
        expected = stats.get('expected_total', 0)
        actual = stats.get('actual_crawled', 0)
        passed = stats.get('verification_passed', False)
        status = '✅' if passed else '⚠️'
        
        if expected > 0:
            print(f"   {status} {category}: {actual}/{expected} 篇")
        else:
            print(f"   ⚪ {category}: {actual} 篇 (无页面总数)")
            
    crawl_verification = {
        "total_expected": total_expected,
        "total_actual": total_actual,
        "verification_passed": verification_passed,
        "category_details": all_stats
    }
    
    # 筛选今天的文章
    print("📅 正在筛选今天的文章...")
    today_papers = filter_today_papers(all_papers)
    print(f"✅ 今天的文章: {len(today_papers)} 篇")
    
    # 按类别统计今天的文章
    gr_qc_today = [p for p in today_papers if p.primary_category == 'gr-qc']
    astro_ph_today = [p for p in today_papers if p.primary_category.startswith('astro-ph')]
    
    print(f"📊 今天的文章分布:")
    print(f"   gr-qc: {len(gr_qc_today)} 篇")
    print(f"   astro-ph: {len(astro_ph_today)} 篇")
    
    # 筛选引力波相关文章
    print("🔍 正在筛选引力波相关文章...")
    gw_papers = filter_gravitational_wave_papers(today_papers)
    print(f"✅ 筛选出 {len(gw_papers)} 篇引力波相关文章")
    
    if len(gw_papers) == 0:
        print("⚠️ 没有找到引力波相关文章")
        return [], ""
    
    # 统计提交类型（基于网页源代码解析）
    submission_stats = {"new": 0, "cross-list": 0, "replaced": 0}
    for paper in gw_papers:
        submission_info = getattr(paper, 'submission_info', {})
        submission_type = submission_info.get('type', 'new')
        submission_stats[submission_type] = submission_stats.get(submission_type, 0) + 1
    
    print(f"📊 引力波论文提交类型:")
    print(f"   🆕 New: {submission_stats.get('new', 0)}")
    print(f"   🔄 Cross-lists: {submission_stats.get('cross-list', 0)}")
    print(f"   🔄 Replacements: {submission_stats.get('replaced', 0)}")
    
    # 获取日期
    date_str = datetime.date.today().strftime('%Y-%m-%d')
    
    # 保存到存档（包含爬取验证统计）
    if ENABLE_ARCHIVE:
        save_to_archive(today_papers, gw_papers, date_str, crawl_verification)
    
    # 生成 digest 文件
    print("📝 正在生成 digest.md...")
    with open('digest.md', 'w', encoding='utf-8') as f:
        f.write(f"# Complete Daily GW arXiv Digest - {date_str}\n\n")
        f.write(f"**总爬取文章**: {len(all_papers)} 篇  \n")
        f.write(f"**今天的文章**: {len(today_papers)} 篇  \n")
        f.write(f"  - gr-qc: {len(gr_qc_today)} 篇  \n")
        f.write(f"  - astro-ph: {len(astro_ph_today)} 篇  \n")
        f.write(f"**引力波相关**: {len(gw_papers)} 篇  \n")
        f.write(f"**提交类型**: 🆕 {submission_stats.get('new', 0)} New • 🔄 {submission_stats.get('cross-list', 0)} Cross-lists • 🔄 {submission_stats.get('replaced', 0)} Replacements  \n")
        f.write("\n")
        
        for i, paper in enumerate(gw_papers, 1):
            arxiv_id = paper.entry_id.split('/')[-1]
            pub_date = paper.published.strftime('%d %b %Y') if paper.published else 'Unknown'
            
            f.write(f"## {i}. {paper.title}\n\n")
            f.write(f"**arXiv**: [{arxiv_id}](https://arxiv.org/abs/{arxiv_id})  \n")
            f.write(f"**Authors**: {', '.join(author['name'] for author in paper.authors)}  \n")
            f.write(f"**Date**: {pub_date}  \n")
            f.write(f"**Categories**: {', '.join(paper.categories)}  \n")
            submission_info = getattr(paper, 'submission_info', {})
            f.write(f"**Type**: {submission_info.get('details', 'new submission')}  \n\n")
            f.write(f"**Abstract**: {paper.summary}  \n\n")
            f.write("---\n\n")
    
    print("✅ digest.md 生成完成")
    
    return gw_papers, date_str

if __name__ == "__main__":
    papers, date_str = main()
    
    # 生成 Mattermost 消息
    if papers:
        print("\n📱 准备 Mattermost 消息...")
        message = format_mattermost_message(papers, date_str)
        
        # 保存预览
        with open('mattermost_preview.md', 'w', encoding='utf-8') as f:
            f.write(message)
        print(f"📋 Mattermost 预览已保存 ({len(message)} 字符)")
        
        # 可选：发送到 Mattermost
        # send_to_mattermost(message)
