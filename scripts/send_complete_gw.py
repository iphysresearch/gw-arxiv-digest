#!/usr/bin/env python3
"""
发送完整的引力波 arXiv digest 到 Mattermost
"""

import sys
from pathlib import Path

# 添加脚本目录到路径
sys.path.append(str(Path(__file__).parent))

from fetch_complete_gw import main, format_mattermost_message, send_to_mattermost

def main_send():
    """主函数：获取完整引力波论文并发送到 Mattermost"""
    print("📡 正在完整爬取引力波相关论文并发送到 Mattermost...")
    
    try:
        # 获取论文
        papers, date_str = main()
        
        if not papers:
            print("⚠️ 没有找到引力波相关论文")
            return False
        
        # 格式化消息
        print("📝 正在格式化 Mattermost 消息...")
        message = format_mattermost_message(papers, date_str)
        
        # 发送到 Mattermost
        print("📤 正在发送到 Mattermost...")
        success = send_to_mattermost(message)
        
        if success:
            print("✅ 成功发送完整引力波 digest 到 Mattermost！")
            return True
        else:
            print("❌ 发送到 Mattermost 失败")
            return False
            
    except Exception as e:
        print(f"❌ 错误: {e}")
        return False

if __name__ == "__main__":
    success = main_send()
    sys.exit(0 if success else 1)
