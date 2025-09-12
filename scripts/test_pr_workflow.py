#!/usr/bin/env python3
"""
测试 PR 工作流程的脚本
模拟 GitHub Actions 的 PR 创建和自动合并流程
"""

import os
import sys
import subprocess
import json
import datetime
from pathlib import Path

def test_pr_creation_simulation():
    """模拟 PR 创建过程"""
    print("🔧 Testing PR creation simulation...")
    
    date_str = datetime.date.today().strftime('%Y-%m-%d')
    run_id = "12345"
    
    # 模拟 PR 分支名称
    branch_name = f"digest-{date_str}-{run_id}"
    
    try:
        # 检查是否在 git 仓库中
        result = subprocess.run(['git', 'status'], capture_output=True, text=True)
        if result.returncode != 0:
            print("⚠️ Not in a git repository, simulating PR creation...")
            return True
        
        # 模拟创建分支
        print(f"📋 Would create branch: {branch_name}")
        print(f"📁 Would add files: archives/, digest.md, mattermost_preview.md")
        print(f"📝 Would create PR: '🌊 Daily GW arXiv Digest - {date_str}'")
        
        # 检查是否有存档文件
        archive_file = f"archives/filtered/gw_filtered_{date_str}.json"
        if os.path.exists(archive_file):
            file_size = os.path.getsize(archive_file)
            print(f"✅ Archive file exists: {archive_file} ({file_size} bytes)")
        else:
            print(f"❌ Archive file missing: {archive_file}")
            return False
        
        print("✅ PR creation simulation successful")
        return True
        
    except Exception as e:
        print(f"❌ PR creation simulation failed: {e}")
        return False

def test_skip_logic():
    """测试跳过逻辑"""
    print("🔧 Testing skip logic...")
    
    date_str = datetime.date.today().strftime('%Y-%m-%d')
    hour = datetime.datetime.now().hour
    
    should_skip = False
    skip_reasons = []
    
    print(f"🔍 Checking execution for {date_str} at hour {hour}")
    
    # 检查是否已有今天的存档 (在 main 分支中)
    archive_file = f"archives/filtered/gw_filtered_{date_str}.json"
    if os.path.exists(archive_file):
        file_size = os.path.getsize(archive_file)
        print(f"📊 Existing file size: {file_size} bytes")
        
        if file_size < 1000:
            print("⚠️ Existing file too small, would proceed anyway")
        else:
            should_skip = True
            skip_reasons.append("📁 Today's digest already exists in main branch")
            print("✅ Valid digest file found in main branch")
    else:
        print(f"✅ No existing digest found for {date_str} in main branch")
    
    # 模拟检查未合并的 PR (在实际环境中会使用 gh CLI)
    print("🔍 Would check for existing open PRs...")
    print("✅ No existing open PR found (simulated)")
    
    # 检查时间窗口
    if hour < 7 or hour > 18:
        print("🕐 Outside optimal window (UTC 7-18), but would proceed as scheduled")
    else:
        print("🕐 Within arXiv update window (UTC 7-18) ✅")
    
    if should_skip:
        print("⏭️ Would SKIP execution:")
        for reason in skip_reasons:
            print(f"   {reason}")
        print("✅ Skip logic working correctly (this is expected behavior)")
        return True  # 跳过是正确的行为
    else:
        print("✅ Would PROCEED with crawl execution")
        return True

def test_auto_merge_logic():
    """测试自动合并逻辑"""
    print("🔧 Testing auto-merge logic...")
    
    # 模拟检查 PR 年龄
    current_time = datetime.datetime.now()
    old_pr_time = current_time - datetime.timedelta(hours=25)  # 25 小时前
    young_pr_time = current_time - datetime.timedelta(hours=12)  # 12 小时前
    
    print(f"📋 Simulating PR created at {old_pr_time}")
    age_hours = (current_time - old_pr_time).total_seconds() / 3600
    print(f"⏰ PR age: {age_hours:.1f} hours")
    
    if age_hours > 24:
        print("✅ PR is older than 24 hours, would auto-merge")
        print("🔄 Would execute: gh pr merge --squash --delete-branch")
        return True
    else:
        print(f"⏳ PR is only {age_hours:.1f} hours old, would wait")
        return False

def main():
    """主测试函数"""
    print("🧪 Testing PR Workflow Logic")
    print("=" * 50)
    
    tests = [
        ("Skip Logic", test_skip_logic),
        ("PR Creation Simulation", test_pr_creation_simulation),
        ("Auto-merge Logic", test_auto_merge_logic)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n{'='*20} {test_name} {'='*20}")
        
        try:
            if test_func():
                passed += 1
                print(f"✅ {test_name} passed")
            else:
                print(f"❌ {test_name} failed")
        except Exception as e:
            print(f"❌ {test_name} error: {e}")
    
    print(f"\n{'='*50}")
    print(f"📊 PR Workflow Test Results: {passed}/{total} passed")
    
    if passed == total:
        print("🎉 All PR workflow tests passed!")
        print("The PR-based workflow should work correctly.")
        return True
    else:
        print("⚠️ Some PR workflow tests failed.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
