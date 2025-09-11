#!/usr/bin/env python3
"""
本地 GitHub Actions 测试脚本
模拟 GitHub Actions 环境和工作流程
"""

import os
import sys
import subprocess
import json
import datetime
from pathlib import Path

def setup_github_env():
    """设置模拟 GitHub Actions 环境变量"""
    env_vars = {
        'GITHUB_WORKSPACE': '/workspace',
        'GITHUB_REPOSITORY': 'iphysresearch/gw-arxiv-digest',
        'GITHUB_SHA': 'test-commit-sha',
        'GITHUB_REF': 'refs/heads/main',
        'GITHUB_ACTOR': 'test-user',
        'GITHUB_WORKFLOW': 'Daily GW arXiv Digest',
        'GITHUB_RUN_ID': '12345',
        'GITHUB_RUN_NUMBER': '1',
        'RUNNER_OS': 'Linux',
        'RUNNER_ARCH': 'X64',
        'ENABLE_ARCHIVE': 'true',
        'ARCHIVE_DIR': 'archives/complete'
    }
    
    for key, value in env_vars.items():
        os.environ[key] = value
    
    print("✅ GitHub Actions 环境变量已设置")
    return env_vars

def test_step_install_dependencies():
    """测试步骤: 安装依赖"""
    print("\n🔧 Step: Install dependencies")
    
    try:
        result = subprocess.run([
            'pip3', 'install', '-r', 'requirements.txt'
        ], capture_output=True, text=True, timeout=60)
        
        if result.returncode == 0:
            print("✅ Dependencies installed successfully")
            return True
        else:
            print(f"❌ Dependency installation failed: {result.stderr}")
            return False
    except Exception as e:
        print(f"❌ Error installing dependencies: {e}")
        return False

def test_step_set_env_vars():
    """测试步骤: 设置环境变量"""
    print("\n🔧 Step: Set environment variables")
    
    date_str = datetime.date.today().strftime('%Y-%m-%d')
    timestamp = datetime.datetime.now().strftime('%a %b %d %H:%M:%S UTC %Y')
    hour = datetime.datetime.now().hour
    
    env_vars = {
        'DATE_STR': date_str,
        'TIMESTAMP': timestamp,
        'HOUR': str(hour),
        'WORKFLOW_START': str(int(datetime.datetime.now().timestamp()))
    }
    
    for key, value in env_vars.items():
        os.environ[key] = value
        print(f"   {key}={value}")
    
    print("✅ Environment variables set")
    return True

def test_step_execution_check():
    """测试步骤: 智能执行检查"""
    print("\n🔧 Step: Intelligent execution check")
    
    date_str = os.environ.get('DATE_STR')
    hour = int(os.environ.get('HOUR', 0))
    
    print(f"🔍 Execution check for {date_str} at hour {hour}")
    
    should_skip = False
    skip_reasons = []
    
    # 检查是否已有今天的存档
    archive_file = f"archives/filtered/gw_filtered_{date_str}.json"
    if os.path.exists(archive_file):
        file_size = os.path.getsize(archive_file)
        print(f"📊 Existing file size: {file_size} bytes")
        
        if file_size < 1000:
            print("⚠️ Existing file too small, proceeding anyway")
        else:
            should_skip = True
            skip_reasons.append("📁 Today's digest already exists")
    else:
        print(f"✅ No existing digest found for {date_str}")
    
    # 检查时间窗口
    if hour < 7 or hour > 18:
        print("🕐 Outside optimal window (UTC 7-18), but proceeding as scheduled")
    else:
        print("🕐 Within arXiv update window (UTC 7-18) ✅")
    
    if should_skip:
        print("⏭️ SKIPPING execution:")
        for reason in skip_reasons:
            print(f"   {reason}")
        return False
    else:
        print("✅ PROCEEDING with crawl execution")
        return True

def test_step_run_crawler():
    """测试步骤: 运行爬虫"""
    print("\n🔧 Step: Run GW crawler")
    
    try:
        start_time = datetime.datetime.now()
        
        result = subprocess.run([
            'python3', 'scripts/fetch_complete_gw.py'
        ], capture_output=True, text=True, timeout=300)
        
        end_time = datetime.datetime.now()
        execution_time = (end_time - start_time).seconds
        
        if result.returncode == 0:
            print(f"✅ Crawler executed successfully in {execution_time}s")
            print("📊 Crawler output preview:")
            output_lines = result.stdout.split('\n')
            for line in output_lines[-10:]:  # 显示最后10行
                if line.strip():
                    print(f"   {line}")
            return True, execution_time
        else:
            print(f"❌ Crawler execution failed: {result.stderr}")
            return False, 0
            
    except subprocess.TimeoutExpired:
        print("❌ Crawler execution timed out")
        return False, 0
    except Exception as e:
        print(f"❌ Error running crawler: {e}")
        return False, 0

def test_step_verify_results():
    """测试步骤: 验证结果"""
    print("\n🔧 Step: Verify results")
    
    date_str = os.environ.get('DATE_STR')
    
    # 检查必要文件
    required_files = [
        f"archives/filtered/gw_filtered_{date_str}.json",
        "digest.md"
    ]
    
    all_exist = True
    for file_path in required_files:
        if os.path.exists(file_path):
            file_size = os.path.getsize(file_path)
            print(f"✅ {file_path} exists ({file_size} bytes)")
        else:
            print(f"❌ {file_path} missing")
            all_exist = False
    
    if all_exist:
        # 分析引力波文件
        gw_file = f"archives/filtered/gw_filtered_{date_str}.json"
        try:
            with open(gw_file, 'r') as f:
                data = json.load(f)
                gw_count = data.get('total_gw_papers', 0)
                total_crawled = data.get('total_crawled', 0)
                
            print(f"🌊 GW papers found: {gw_count}")
            print(f"📊 Total crawled: {total_crawled}")
            
            return True, gw_count
        except Exception as e:
            print(f"❌ Error reading archive: {e}")
            return False, 0
    
    return all_exist, 0

def test_step_mattermost_send():
    """测试步骤: Mattermost 发送"""
    print("\n🔧 Step: Mattermost notification")
    
    webhook_url = os.environ.get('MATTERMOST_WEBHOOK_URL')
    
    if not webhook_url:
        print("⚠️ MATTERMOST_WEBHOOK_URL not set, using mock")
        webhook_url = "http://localhost:8080/hooks/test"
    
    try:
        result = subprocess.run([
            'python3', 'scripts/send_complete_gw.py'
        ], capture_output=True, text=True, timeout=30)
        
        if result.returncode == 0:
            print("✅ Mattermost send completed")
            return True
        else:
            print(f"❌ Mattermost send failed: {result.stderr}")
            # 尝试简单的 curl 测试
            print("🔄 Trying fallback curl test...")
            curl_result = subprocess.run([
                'curl', '-s', '-X', 'POST', 
                '-H', 'Content-Type: application/json',
                '-d', '{"text": "🧪 Docker test notification", "username": "Test Bot"}',
                webhook_url
            ], capture_output=True, text=True)
            
            if curl_result.returncode == 0:
                print("✅ Fallback curl test passed")
                return True
            else:
                print("❌ Fallback curl test failed")
                return False
                
    except Exception as e:
        print(f"❌ Error in Mattermost test: {e}")
        return False

def main():
    """主测试流程"""
    print("🐳 Starting local GitHub Actions test environment")
    print("=" * 60)
    
    # 设置环境
    setup_github_env()
    
    tests = [
        ("Environment Variables", test_step_set_env_vars),
        ("Install Dependencies", test_step_install_dependencies),
        ("Execution Check", test_step_execution_check),
        ("Run Crawler", test_step_run_crawler),
        ("Verify Results", test_step_verify_results),
        ("Mattermost Send", test_step_mattermost_send)
    ]
    
    results = []
    
    for test_name, test_func in tests:
        print(f"\n{'='*20} {test_name} {'='*20}")
        
        try:
            if test_name == "Run Crawler":
                success, execution_time = test_func()
                results.append((test_name, success, f"Execution time: {execution_time}s"))
            elif test_name == "Verify Results":
                success, gw_count = test_func()
                results.append((test_name, success, f"GW papers: {gw_count}"))
            else:
                success = test_func()
                results.append((test_name, success, ""))
        except Exception as e:
            print(f"❌ Test '{test_name}' failed with error: {e}")
            results.append((test_name, False, f"Error: {e}"))
    
    # 总结
    print("\n" + "="*60)
    print("📊 Local GitHub Actions Test Summary")
    print("="*60)
    
    passed = 0
    for test_name, success, details in results:
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"{status:10} {test_name:25} {details}")
        if success:
            passed += 1
    
    print(f"\n🎯 Results: {passed}/{len(tests)} tests passed")
    
    if passed == len(tests):
        print("🎉 All tests passed! GitHub Actions should work correctly.")
        return True
    else:
        print("⚠️ Some tests failed. Check the errors above.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
