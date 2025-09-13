#!/usr/bin/env python3
"""
调试 GitHub Actions 执行问题
分析为什么爬虫步骤被跳过
"""

import os
import sys
import subprocess
import datetime
from pathlib import Path

def check_file_dates():
    """检查存档文件的日期"""
    print("🔍 Checking archive file dates...")
    
    archives_dir = Path("archives/filtered")
    if not archives_dir.exists():
        print("❌ Archives directory doesn't exist")
        return
    
    json_files = list(archives_dir.glob("gw_filtered_*.json"))
    
    if not json_files:
        print("❌ No archive files found")
        return
    
    print(f"📁 Found {len(json_files)} archive files:")
    
    for file_path in sorted(json_files):
        try:
            # 获取文件修改时间
            file_stat = file_path.stat()
            file_mtime = datetime.datetime.fromtimestamp(file_stat.st_mtime)
            file_size = file_stat.st_size
            
            # 从文件名提取日期
            filename_date = file_path.stem.replace('gw_filtered_', '')
            
            print(f"   📄 {file_path.name}")
            print(f"      📅 文件名日期: {filename_date}")
            print(f"      🕐 修改时间: {file_mtime.strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"      📊 文件大小: {file_size} bytes")
            print()
            
        except Exception as e:
            print(f"   ❌ Error reading {file_path}: {e}")

def simulate_execution_check():
    """模拟执行检查逻辑"""
    print("🔧 Simulating execution check logic...")
    
    # 模拟 GitHub Actions 环境
    date_str = "2025-09-13"  # 从日志中看到的日期
    hour = 2  # 从日志中看到的小时
    
    print(f"📅 Checking for date: {date_str}")
    print(f"🕐 Hour: {hour}")
    
    should_skip = False
    skip_reasons = []
    
    # 检查存档文件
    archive_file = f"archives/filtered/gw_filtered_{date_str}.json"
    print(f"🔍 Looking for file: {archive_file}")
    
    if os.path.exists(archive_file):
        try:
            file_stat = os.stat(archive_file)
            file_size = file_stat.st_size
            file_mtime = datetime.datetime.fromtimestamp(file_stat.st_mtime)
            file_date = file_mtime.strftime('%Y-%m-%d')
            
            print(f"📊 Found existing file:")
            print(f"   📁 File: {archive_file}")
            print(f"   📅 File date: {file_date}")
            print(f"   📊 File size: {file_size} bytes")
            print(f"   🕐 Current date: {date_str}")
            
            # 应用逻辑
            if file_date == date_str and file_size > 1000:
                should_skip = True
                skip_reasons.append("📁 Valid digest for today already exists")
                print("✅ Valid digest file found for today")
            else:
                print("⚠️ File exists but may be outdated or corrupted - proceeding")
                print(f"   📅 File date: {file_date} vs Current: {date_str}")
                print(f"   📊 File size: {file_size} bytes")
        except Exception as e:
            print(f"❌ Error checking file: {e}")
    else:
        print(f"✅ No existing digest found for {date_str}")
    
    # 检查时间窗口
    if hour < 7 or hour > 18:
        print("🕐 Outside optimal window (UTC 7-18), but proceeding as scheduled")
    else:
        print("🕐 Within arXiv update window (UTC 7-18) ✅")
    
    print(f"\n📊 Result: skip_execution={should_skip}")
    
    if should_skip:
        print("⏭️ SKIPPING execution:")
        for reason in skip_reasons:
            print(f"   {reason}")
    else:
        print("✅ PROCEEDING with crawl execution")
    
    return should_skip

def check_github_actions_environment():
    """检查 GitHub Actions 环境变量"""
    print("🔧 Checking GitHub Actions environment...")
    
    # 模拟从日志中看到的环境
    github_env = {
        'DATE_STR': '2025-09-13',
        'TIMESTAMP': 'Sat Sep 13 02:23:06 UTC 2025',
        'HOUR': '02',
        'WORKFLOW_START': '1757730186'
    }
    
    print("📋 Environment variables from logs:")
    for key, value in github_env.items():
        print(f"   {key}={value}")
    
    # 检查时区问题
    utc_time = datetime.datetime.strptime("2025-09-13 02:23:06", "%Y-%m-%d %H:%M:%S")
    print(f"\n🕐 UTC time from logs: {utc_time}")
    print(f"🕐 Local time now: {datetime.datetime.now()}")
    
    # 检查是否是时区导致的日期问题
    local_date = datetime.datetime.now().strftime('%Y-%m-%d')
    utc_date = utc_time.strftime('%Y-%m-%d')
    
    print(f"📅 Local date: {local_date}")
    print(f"📅 UTC date from logs: {utc_date}")
    
    if local_date != utc_date:
        print("⚠️ Date mismatch detected! This could be the issue.")
        return False
    else:
        print("✅ Dates match")
        return True

def main():
    """主函数"""
    print("🐛 Debugging GitHub Actions Execution Issue")
    print("=" * 60)
    print("Analyzing why the crawler steps were skipped")
    print("=" * 60)
    
    # 检查文件日期
    check_file_dates()
    print()
    
    # 检查环境
    env_ok = check_github_actions_environment()
    print()
    
    # 模拟执行检查
    would_skip = simulate_execution_check()
    print()
    
    # 分析结果
    print("=" * 60)
    print("📊 Analysis Results")
    print("=" * 60)
    
    if would_skip:
        print("❌ Problem identified: Execution would be skipped")
        print("💡 Possible causes:")
        print("   1. Archive file from previous day exists")
        print("   2. File date check logic issue")
        print("   3. Time zone mismatch")
        print()
        print("🔧 Suggested fixes:")
        print("   1. Improve date checking logic")
        print("   2. Add more debug output to workflow")
        print("   3. Consider UTC vs local time issues")
    else:
        print("✅ Execution check would proceed normally")
        print("💡 The issue might be elsewhere:")
        print("   1. Workflow step conditions")
        print("   2. GitHub Actions permissions")
        print("   3. Network connectivity issues")
    
    return not would_skip

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
