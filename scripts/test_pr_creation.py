#!/usr/bin/env python3
"""
测试 PR 创建功能
模拟 GitHub Actions 环境中的 PR 创建过程
"""

import os
import json
import subprocess
import tempfile
import shutil
from datetime import datetime

def test_pr_creation():
    """测试 PR 创建功能"""
    print("🧪 Testing PR Creation Functionality")
    print("=" * 50)
    
    # 设置测试环境
    test_date = "2025-09-13"
    test_dir = tempfile.mkdtemp(prefix="gw-arxiv-test-")
    
    try:
        print(f"📁 Test directory: {test_dir}")
        
        # 复制当前目录到测试目录（包括 .git）
        print("📋 Copying project files...")
        for item in os.listdir('.'):
            if item not in ['__pycache__', '.env']:
                src = os.path.join('.', item)
                dst = os.path.join(test_dir, item)
                if os.path.isdir(src):
                    shutil.copytree(src, dst)
                else:
                    shutil.copy2(src, dst)
        
        # 切换到测试目录
        os.chdir(test_dir)
        print(f"📂 Changed to: {os.getcwd()}")
        
        # 清理可能存在的文件
        print("🧹 Cleaning existing files...")
        for file in ['digest.md', 'mattermost_preview.md']:
            if os.path.exists(file):
                os.remove(file)
                print(f"   Removed: {file}")
        
        # 清理存档目录
        if os.path.exists('archives'):
            shutil.rmtree('archives')
            print("   Removed: archives/")
        
        # 运行爬虫生成文件
        print("\n🚀 Running crawler to generate files...")
        result = subprocess.run(['python', 'scripts/fetch_complete_gw.py'], 
                              capture_output=True, text=True, cwd=test_dir)
        
        if result.returncode != 0:
            print(f"❌ Crawler failed: {result.stderr}")
            return False
        
        print("✅ Crawler completed successfully")
        
        # 检查生成的文件
        print("\n📋 Checking generated files...")
        required_files = [
            'digest.md',
            'mattermost_preview.md',
            f'archives/filtered/gw_filtered_{test_date}.json',
            f'archives/complete/gr_qc_{test_date}.json',
            f'archives/complete/astro_ph_{test_date}.json'
        ]
        
        all_files_exist = True
        for file_path in required_files:
            if os.path.exists(file_path):
                size = os.path.getsize(file_path)
                print(f"   ✅ {file_path} ({size} bytes)")
            else:
                print(f"   ❌ {file_path} - MISSING")
                all_files_exist = False
        
        if not all_files_exist:
            print("❌ Some required files are missing")
            return False
        
        # 模拟 peter-evans/create-pull-request 的行为
        print("\n🔍 Simulating peter-evans/create-pull-request behavior...")
        
        # 检查 git status
        result = subprocess.run(['git', 'status', '--porcelain'], 
                              capture_output=True, text=True, cwd=test_dir)
        
        if result.returncode != 0:
            print(f"❌ Git status failed: {result.stderr}")
            return False
        
        print("📊 Git status output:")
        print(result.stdout)
        
        # 检查特定文件
        for file_path in required_files:
            result = subprocess.run(['git', 'status', '--porcelain', '--', file_path], 
                                  capture_output=True, text=True, cwd=test_dir)
            if result.stdout.strip():
                print(f"   ✅ {file_path} - detected by git")
            else:
                print(f"   ⚠️ {file_path} - not detected by git")
        
        # 模拟添加文件到 git (使用 force add)
        print("\n📝 Simulating git add -f...")
        for file_path in required_files:
            if os.path.exists(file_path):
                result = subprocess.run(['git', 'add', '-f', file_path], 
                                      capture_output=True, text=True, cwd=test_dir)
                if result.returncode == 0:
                    print(f"   ✅ Force added: {file_path}")
                else:
                    print(f"   ❌ Failed to force add: {file_path}")
                    print(f"       Error: {result.stderr}")
        
        # 检查暂存区
        result = subprocess.run(['git', 'status', '--porcelain'], 
                              capture_output=True, text=True, cwd=test_dir)
        print(f"\n📊 Final git status:")
        print(result.stdout)
        
        if result.stdout.strip():
            print("✅ Files are ready for commit and PR creation")
            return True
        else:
            print("❌ No files staged for commit")
            return False
            
    except Exception as e:
        print(f"❌ Test failed with error: {e}")
        return False
    finally:
        # 清理测试目录
        print(f"\n🧹 Cleaning up test directory: {test_dir}")
        shutil.rmtree(test_dir)
        os.chdir('/Users/herb/Github/gw-arxiv-digest')

if __name__ == "__main__":
    success = test_pr_creation()
    if success:
        print("\n🎉 PR creation test PASSED!")
    else:
        print("\n❌ PR creation test FAILED!")
        exit(1)
