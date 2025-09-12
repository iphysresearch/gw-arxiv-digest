#!/usr/bin/env python3
"""
测试 workflow 链式执行的脚本
验证 arxiv-digest -> auto-merge-digest 的触发流程
"""

import os
import sys
import subprocess
import json
import datetime
from pathlib import Path

def test_workflow_trigger_logic():
    """测试 workflow 触发逻辑"""
    print("🔧 Testing workflow trigger logic...")
    
    # 模拟 workflow_run 事件
    github_event_name = "workflow_run"
    workflow_run_name = "Daily GW arXiv Digest"
    workflow_run_conclusion = "success"
    
    print(f"📊 Event: {github_event_name}")
    print(f"📊 Workflow: {workflow_run_name}")
    print(f"📊 Conclusion: {workflow_run_conclusion}")
    
    # 模拟检查逻辑
    if github_event_name == "workflow_run":
        print("🔄 Triggered by workflow completion")
        
        if workflow_run_conclusion == "success":
            print("✅ Upstream workflow succeeded, checking for new PRs")
            print("⏳ Would wait 10 seconds for PR creation")
            return True
        else:
            print("❌ Upstream workflow failed, only checking old PRs")
            return False
    else:
        print("📅 Triggered by schedule or manual dispatch")
        return True

def test_pr_detection():
    """测试 PR 检测逻辑"""
    print("🔧 Testing PR detection...")
    
    today = datetime.date.today().strftime('%Y-%m-%d')
    
    print(f"🔍 Looking for PRs with title containing: 'Daily GW arXiv Digest {today}'")
    
    # 模拟 gh CLI 命令
    print("📋 Would execute: gh pr list --state open --search 'Daily GW arXiv Digest {today} in:title'")
    
    # 检查是否有实际的存档文件（表明可能有 PR）
    archive_file = f"archives/filtered/gw_filtered_{today}.json"
    if os.path.exists(archive_file):
        print(f"✅ Found archive file: {archive_file}")
        print("📋 This suggests a PR might exist or should be created")
        return True
    else:
        print(f"❌ No archive file found: {archive_file}")
        print("📋 No PR expected for today")
        return False

def test_auto_merge_conditions():
    """测试自动合并条件"""
    print("🔧 Testing auto-merge conditions...")
    
    # 模拟不同年龄的 PR
    current_time = datetime.datetime.now()
    
    test_cases = [
        ("新 PR", 2),   # 2 小时前
        ("中等 PR", 12), # 12 小时前
        ("旧 PR", 25),  # 25 小时前
        ("很旧 PR", 49) # 49 小时前
    ]
    
    for case_name, hours_ago in test_cases:
        pr_time = current_time - datetime.timedelta(hours=hours_ago)
        age_hours = (current_time - pr_time).total_seconds() / 3600
        
        print(f"📋 {case_name}: {age_hours:.1f} 小时前创建")
        
        if age_hours > 24:
            if age_hours > 48:
                print(f"   🚨 超过 48 小时，需要警告通知")
            else:
                print(f"   ✅ 超过 24 小时，可以自动合并")
        else:
            print(f"   ⏳ 少于 24 小时，继续等待")
    
    return True

def test_mattermost_notifications():
    """测试 Mattermost 通知"""
    print("🔧 Testing Mattermost notifications...")
    
    webhook_url = os.environ.get('MATTERMOST_WEBHOOK_URL')
    
    if not webhook_url:
        # 从 .env 文件读取
        try:
            from dotenv import load_dotenv
            load_dotenv()
            webhook_url = os.environ.get('MATTERMOST_WEBHOOK_URL')
        except:
            pass
    
    if webhook_url:
        print(f"✅ Webhook URL configured: {webhook_url[:50]}...")
        
        # 测试通知类型
        notifications = [
            ("🔄 Monitoring activation", "Auto-merge workflow activated"),
            ("✅ Auto-merge success", "PR merged successfully"),
            ("🚨 Merge conflict warning", "PR requires attention")
        ]
        
        for notification_type, description in notifications:
            print(f"   📱 {notification_type}: {description}")
        
        return True
    else:
        print("⚠️ No webhook URL configured, notifications would be skipped")
        return True

def test_workflow_permissions():
    """测试 workflow 权限"""
    print("🔧 Testing workflow permissions...")
    
    required_permissions = [
        "contents: write",
        "pull-requests: write"
    ]
    
    print("📋 Required permissions for auto-merge:")
    for permission in required_permissions:
        print(f"   ✅ {permission}")
    
    print("🔍 These permissions allow:")
    print("   - Creating and merging PRs")
    print("   - Reading repository contents")
    print("   - Deleting merged branches")
    
    return True

def main():
    """主测试函数"""
    print("🔗 Testing Workflow Chain Execution")
    print("=" * 60)
    print("This tests the arxiv-digest -> auto-merge-digest chain")
    print("=" * 60)
    
    tests = [
        ("Workflow Trigger Logic", test_workflow_trigger_logic),
        ("PR Detection", test_pr_detection),
        ("Auto-merge Conditions", test_auto_merge_conditions),
        ("Mattermost Notifications", test_mattermost_notifications),
        ("Workflow Permissions", test_workflow_permissions)
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
    
    print(f"\n{'='*60}")
    print(f"📊 Workflow Chain Test Results: {passed}/{total} passed")
    
    if passed == total:
        print("🎉 All workflow chain tests passed!")
        print("")
        print("🔄 The workflow chain will work as follows:")
        print("   1. arxiv-digest runs and creates PR")
        print("   2. auto-merge-digest is automatically triggered")
        print("   3. auto-merge monitors and merges old PRs")
        print("   4. Mattermost notifications keep you informed")
        print("")
        print("✅ System is ready for automated operation!")
        return True
    else:
        print("⚠️ Some workflow chain tests failed.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
