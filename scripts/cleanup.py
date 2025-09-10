#!/usr/bin/env python3
"""
清理脚本 - 确保推送后只保留 archives 新增的 JSON 文件
"""

import os
from pathlib import Path

def cleanup_generated_files():
    """清理生成的文件，只保留 archives 中的 JSON 文件"""
    
    # 要清理的文件列表
    files_to_clean = [
        'digest.md',
        'digest_ai.md', 
        'mattermost_preview.md'
    ]
    
    # 要清理的目录列表
    dirs_to_clean = [
        'scripts/__pycache__'
    ]
    
    cleaned_count = 0
    
    # 清理文件
    for file_path in files_to_clean:
        if os.path.exists(file_path):
            try:
                os.remove(file_path)
                print(f"🗑️  已删除文件: {file_path}")
                cleaned_count += 1
            except Exception as e:
                print(f"❌ 删除文件 {file_path} 失败: {e}")
    
    # 清理目录
    for dir_path in dirs_to_clean:
        if os.path.exists(dir_path):
            try:
                import shutil
                shutil.rmtree(dir_path)
                print(f"🗑️  已删除目录: {dir_path}")
                cleaned_count += 1
            except Exception as e:
                print(f"❌ 删除目录 {dir_path} 失败: {e}")
    
    # 清理所有 Python 缓存文件
    import subprocess
    try:
        subprocess.run(['find', '.', '-name', '*.pyc', '-delete'], check=False, capture_output=True)
        subprocess.run(['find', '.', '-name', '__pycache__', '-type', 'd', '-exec', 'rm', '-rf', '{}', '+'], check=False, capture_output=True)
        print("🗑️  已清理 Python 缓存文件")
    except:
        pass
    
    # 检查 archives 目录
    archives_dir = Path('archives')
    if archives_dir.exists():
        # 检查所有子目录
        subdirs = ['complete', 'filtered', 'arxiv']
        total_json_files = 0
        
        print(f"📁 archives 目录状态:")
        for subdir in subdirs:
            subdir_path = archives_dir / subdir
            if subdir_path.exists():
                json_files = list(subdir_path.glob('*.json'))
                total_json_files += len(json_files)
                print(f"   {subdir}/: {len(json_files)} 个 JSON 文件")
                
                # 列出最新的 JSON 文件
                if json_files:
                    latest_json = max(json_files, key=os.path.getmtime)
                    print(f"      最新文件: {latest_json.name}")
        
        index_files = list(archives_dir.glob('*.md'))
        print(f"   README/索引文件: {len(index_files)} 个")
        print(f"   总计 JSON 文件: {total_json_files} 个")
    
    if cleaned_count > 0:
        print(f"✅ 清理完成，删除了 {cleaned_count} 个项目")
    else:
        print("✅ 没有需要清理的文件")

def main():
    """主函数"""
    print("🧹 开始清理生成的文件...")
    cleanup_generated_files()
    print("🎯 清理完成，项目状态已重置")

if __name__ == "__main__":
    main()
