#!/usr/bin/env python3
"""
完整系统验证脚本
验证网页爬虫自检功能和分类存档功能
"""

import sys
import os
import json
import datetime
from pathlib import Path

# 添加脚本目录到 Python 路径
sys.path.insert(0, str(Path(__file__).parent / 'scripts'))

def test_web_scraper_import():
    """测试网页爬虫模块导入"""
    print("🧪 测试网页爬虫模块导入...")
    try:
        from arxiv_web_scraper import ArxivWebScraper, Client, Search
        print("✅ 网页爬虫模块导入成功")
        return True
    except ImportError as e:
        print(f"❌ 网页爬虫模块导入失败: {e}")
        return False

def test_single_category_crawl():
    """测试单个类别爬取和自检功能"""
    print("\n🧪 测试单个类别爬取和自检功能...")
    
    try:
        from arxiv_web_scraper import ArxivWebScraper
        scraper = ArxivWebScraper()
        
        # 测试 gr-qc 类别
        print("📡 测试 gr-qc 类别...")
        papers, stats = scraper.fetch_category_new('gr-qc')
        
        print(f"📊 爬取结果: {len(papers)} 篇论文")
        print(f"📊 期望数量: {stats.get('expected_total', 'unknown')} 篇")
        print(f"📊 页面信息: {stats.get('page_source_info', 'none')}")
        print(f"🔍 验证状态: {'✅ 通过' if stats.get('verification_passed') else '⚠️ 异常'}")
        
        # 验证自检功能
        if stats.get('expected_total', 0) > 0:
            expected = stats['expected_total']
            actual = stats['actual_crawled']
            tolerance = 5
            
            if abs(expected - actual) <= tolerance:
                print("✅ 自检功能正常: 爬取数量与页面显示一致")
                return True, papers, stats
            else:
                print(f"⚠️ 自检发现数量差异: 页面显示{expected}篇，实际爬取{actual}篇")
                return False, papers, stats
        else:
            print("⚠️ 无法从页面获取总数信息")
            return len(papers) > 0, papers, stats
            
    except Exception as e:
        print(f"❌ 测试失败: {e}")
        return False, [], {}

def test_complete_system():
    """测试完整系统"""
    print("\n🧪 测试完整系统...")
    
    try:
        # 设置环境变量以启用存档
        os.environ['ENABLE_ARCHIVE'] = 'true'
        os.environ['ARCHIVE_DIR'] = 'archives/complete'
        
        from fetch_complete_gw import main
        
        print("🚀 运行完整系统测试...")
        papers, date_str = main()
        
        print(f"✅ 完整系统测试完成: 获得 {len(papers)} 篇引力波论文")
        return True, papers, date_str
        
    except Exception as e:
        print(f"❌ 完整系统测试失败: {e}")
        return False, [], ""

def verify_archive_structure():
    """验证存档文件结构"""
    print("\n🧪 验证存档文件结构...")
    
    date_str = datetime.date.today().strftime('%Y-%m-%d')
    archive_dir = Path('archives/complete')
    
    expected_files = [
        f"filtered/gw_filtered_{date_str}.json",  # 筛选后的引力波论文
        f"complete/gr_qc_{date_str}.json",        # 完整GR-QC论文
        f"complete/astro_ph_{date_str}.json"      # 完整Astro-Ph论文
    ]
    
    found_files = []
    missing_files = []
    
    for relative_filename in expected_files:
        file_path = Path('archives') / relative_filename
        filename = relative_filename.split('/')[-1]  # 获取文件名部分
        
        if file_path.exists():
            found_files.append(relative_filename)
            print(f"✅ 找到存档文件: {relative_filename}")
            
            # 验证文件内容
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    
                if 'gw_filtered' in filename:
                    # 验证引力波筛选存档文件
                    if 'crawl_verification' in data:
                        print(f"   🔍 包含爬取验证信息")
                    if 'summary' in data:
                        summary = data['summary']
                        print(f"   📊 总爬取: {summary.get('total_crawled', 0)} 篇")
                        print(f"   📊 引力波: {summary.get('total_gw_papers', 0)} 篇")
                    
                elif 'gr_qc' in filename:
                    # 验证 GR-QC 存档
                    total = data.get('total_papers', 0)
                    gw_related = data.get('gw_related_papers', 0) 
                    print(f"   📊 GR-QC: {total} 篇总计，{gw_related} 篇引力波相关")
                    
                elif 'astro_ph' in filename:
                    # 验证 Astro-Ph 存档
                    total = data.get('total_papers', 0)
                    gw_related = data.get('gw_related_papers', 0)
                    subcats = data.get('subcategories', [])
                    print(f"   📊 Astro-Ph: {total} 篇总计，{gw_related} 篇引力波相关")
                    print(f"   📊 子类别: {len(subcats)} 个")
                    
            except Exception as e:
                print(f"   ❌ 文件格式验证失败: {e}")
                
        else:
            missing_files.append(relative_filename)
            print(f"⚠️ 缺少存档文件: {relative_filename}")
    
    if len(found_files) == len(expected_files):
        print("✅ 所有存档文件都已创建且格式正确")
        return True
    else:
        print(f"⚠️ 找到 {len(found_files)}/{len(expected_files)} 个存档文件")
        return False

def verify_crawl_targets():
    """验证爬取目标达成情况"""
    print("\n🧪 验证爬取目标达成情况...")
    
    date_str = datetime.date.today().strftime('%Y-%m-%d')
    filtered_file = Path('archives/filtered') / f"gw_filtered_{date_str}.json"
    
    if not filtered_file.exists():
        print("❌ 引力波筛选存档文件不存在，无法进行验证")
        return False
    
    try:
        with open(filtered_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        verification = data.get('crawl_verification', {})
        details = verification.get('category_details', [])
        
        gr_qc_count = sum(d.get('actual_crawled', 0) for d in details if d.get('category', '') == 'gr-qc')
        astro_details = [d for d in details if d.get('category', '').startswith('astro-ph')]
        astro_passed = sum(1 for d in astro_details if d.get('verification_passed', False))
        astro_total = len(astro_details)
        
        print(f"📊 GR-QC: {gr_qc_count} 篇 (目标: 47篇)")
        print(f"📊 Astro-Ph子类别验证: {astro_passed}/{astro_total} 个通过")
        
        for d in astro_details[:3]:  # 显示前3个子类别
            category = d.get('category', '?')
            expected = d.get('expected_total', 0)
            actual = d.get('actual_crawled', 0)
            passed = d.get('verification_passed', False)
            print(f"   {category}: {actual}/{expected} 篇 {'✅' if passed else '⚠️'}")
        
        if len(astro_details) > 3:
            print(f"   ... 其余 {len(astro_details)-3} 个子类别")
        
        gr_qc_ok = 35 <= gr_qc_count <= 60
        astro_ok = astro_passed == astro_total  # 所有子类别验证都通过
        
        print(f"🎯 GR-QC 目标达成: {'✅' if gr_qc_ok else '⚠️'}")
        print(f"🎯 Astro-Ph子类别验证: {'✅' if astro_ok else '⚠️'} ({astro_passed}/{astro_total})")
        
        total_expected = verification.get('total_expected', 0)
        total_actual = verification.get('total_actual', 0)
        verification_passed = verification.get('verification_passed', False)
        
        print(f"🔍 页面验证: {'✅ 通过' if verification_passed else '⚠️ 异常'}")
        print(f"🔍 总数对比: {total_actual}/{total_expected} 篇")
        
        return gr_qc_ok and astro_ok and verification_passed
        
    except Exception as e:
        print(f"❌ 验证失败: {e}")
        return False

def main():
    """主测试函数"""
    print("🚀 完整系统验证测试")
    print("=" * 50)
    
    success_count = 0
    total_tests = 5
    
    # 测试1: 模块导入
    if test_web_scraper_import():
        success_count += 1
    
    # 测试2: 单个类别爬取和自检
    crawl_success, papers, stats = test_single_category_crawl()
    if crawl_success:
        success_count += 1
    
    # 测试3: 完整系统
    system_success, all_papers, date_str = test_complete_system()
    if system_success:
        success_count += 1
    
    # 测试4: 存档文件结构
    if verify_archive_structure():
        success_count += 1
    
    # 测试5: 爬取目标验证
    if verify_crawl_targets():
        success_count += 1
    
    # 结果总结
    print("\n" + "=" * 50)
    print("🎉 系统验证完成!")
    print(f"📊 通过测试: {success_count}/{total_tests}")
    
    if success_count == total_tests:
        print("✅ 所有测试通过！系统运行正常。")
        print("\n🎯 关键功能验证:")
        print("  ✅ 网页爬虫自检功能正常")
        print("  ✅ 按类别分类存档功能正常") 
        print("  ✅ 爬取数量验证功能正常")
        print("  ✅ 存档文件结构完整")
        return 0
    else:
        print(f"⚠️ {total_tests - success_count} 个测试未通过，系统需要进一步检查。")
        return 1

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
