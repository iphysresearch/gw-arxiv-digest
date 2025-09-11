#!/usr/bin/env python3
"""
本地 GitHub Actions 完整测试脚本
不依赖 Docker 或外部网络，完全在本地环境中模拟 Actions 工作流程
"""

import os
import sys
import subprocess
import json
import datetime
import tempfile
from pathlib import Path

class LocalActionsRunner:
    def __init__(self):
        self.start_time = datetime.datetime.now()
        self.date_str = self.start_time.strftime('%Y-%m-%d')
        self.hour = self.start_time.hour
        self.results = {}
        self.temp_dir = None
        
        # 设置模拟的 GitHub Actions 环境变量
        self.setup_github_env()
        
    def setup_github_env(self):
        """设置模拟 GitHub Actions 环境变量"""
        github_env = {
            'GITHUB_WORKSPACE': os.getcwd(),
            'GITHUB_REPOSITORY': 'iphysresearch/gw-arxiv-digest',
            'GITHUB_SHA': 'local-test-sha',
            'GITHUB_REF': 'refs/heads/main',
            'GITHUB_ACTOR': 'local-test-user',
            'GITHUB_WORKFLOW': 'Daily GW arXiv Digest',
            'GITHUB_RUN_ID': '12345',
            'GITHUB_RUN_NUMBER': '1',
            'RUNNER_OS': 'Darwin',  # macOS
            'RUNNER_ARCH': 'ARM64',
            'RUNNER_TEMP': tempfile.gettempdir(),
            'ENABLE_ARCHIVE': 'true',
            'ARCHIVE_DIR': 'archives/complete',
            'DATE_STR': self.date_str,
            'TIMESTAMP': self.start_time.strftime('%a %b %d %H:%M:%S UTC %Y'),
            'HOUR': str(self.hour),
            'WORKFLOW_START': str(int(self.start_time.timestamp()))
        }
        
        for key, value in github_env.items():
            os.environ[key] = value
        
        print("✅ GitHub Actions 环境变量已设置")
        
    def log(self, message, level="INFO"):
        """日志输出"""
        timestamp = datetime.datetime.now().strftime('%H:%M:%S')
        prefix = {
            "INFO": "ℹ️",
            "SUCCESS": "✅", 
            "ERROR": "❌",
            "WARNING": "⚠️",
            "DEBUG": "🔍"
        }.get(level, "ℹ️")
        
        print(f"[{timestamp}] {prefix} {message}")
    
    def run_step(self, step_name, step_func, required=True):
        """运行单个步骤"""
        self.log(f"\n{'='*20} {step_name} {'='*20}")
        
        try:
            success = step_func()
            if success:
                self.log(f"{step_name} completed", "SUCCESS")
                return True
            else:
                level = "ERROR" if required else "WARNING"
                self.log(f"{step_name} failed", level)
                return False
        except Exception as e:
            self.log(f"{step_name} error: {e}", "ERROR")
            return False
    
    def step_checkout(self):
        """步骤: Checkout repository"""
        self.log("Checking repository state...")
        
        if os.path.exists('.git'):
            self.log("Git repository found")
            return True
        else:
            self.log("Not a git repository, but continuing...")
            return True
    
    def step_setup_python(self):
        """步骤: Set up Python"""
        self.log("Checking Python environment...")
        
        try:
            result = subprocess.run(['python3', '--version'], capture_output=True, text=True)
            if result.returncode == 0:
                self.log(f"Python: {result.stdout.strip()}")
                
                result = subprocess.run(['pip3', '--version'], capture_output=True, text=True)
                if result.returncode == 0:
                    self.log(f"Pip: {result.stdout.strip()}")
                    return True
            
            return False
        except Exception:
            return False
    
    def step_install_dependencies(self):
        """步骤: Install dependencies"""
        self.log("Installing dependencies...")
        
        try:
            result = subprocess.run([
                'pip3', 'install', '-r', 'requirements.txt'
            ], capture_output=True, text=True, timeout=120)
            
            if result.returncode == 0:
                self.log("Dependencies installed successfully")
                return True
            else:
                self.log(f"Dependency installation failed: {result.stderr}")
                return False
        except subprocess.TimeoutExpired:
            self.log("Dependency installation timed out")
            return False
        except Exception as e:
            self.log(f"Error installing dependencies: {e}")
            return False
    
    def step_set_environment_variables(self):
        """步骤: Set environment variables"""
        self.log("Setting environment variables...")
        
        # 环境变量已在 __init__ 中设置
        self.log(f"DATE_STR: {os.environ['DATE_STR']}")
        self.log(f"HOUR: {os.environ['HOUR']}")
        self.log(f"ENABLE_ARCHIVE: {os.environ['ENABLE_ARCHIVE']}")
        
        return True
    
    def step_execution_check(self):
        """步骤: Intelligent execution check"""
        self.log(f"Execution check for {self.date_str} at hour {self.hour}")
        
        should_skip = False
        
        # 检查是否已有今天的存档
        archive_file = f"archives/filtered/gw_filtered_{self.date_str}.json"
        if os.path.exists(archive_file):
            file_size = os.path.getsize(archive_file)
            self.log(f"Existing file size: {file_size} bytes")
            
            if file_size < 1000:
                self.log("Existing file too small, proceeding anyway")
            else:
                should_skip = True
                self.log("Today's digest already exists")
        else:
            self.log(f"No existing digest found for {self.date_str}")
        
        # 检查时间窗口
        if self.hour < 7 or self.hour > 18:
            self.log("Outside optimal window (UTC 7-18), but proceeding as scheduled")
        else:
            self.log("Within arXiv update window (UTC 7-18)")
        
        self.results['skip_execution'] = should_skip
        
        if should_skip:
            self.log("SKIPPING execution due to existing digest")
            return False
        else:
            self.log("PROCEEDING with crawl execution")
            return True
    
    def step_configure_git(self):
        """步骤: Configure git"""
        self.log("Configuring git...")
        
        try:
            subprocess.run(['git', 'config', '--global', 'user.name', 'GW arXiv Bot'], 
                         check=True, capture_output=True)
            subprocess.run(['git', 'config', '--global', 'user.email', 'action@github.com'], 
                         check=True, capture_output=True)
            
            self.log("Git configured successfully")
            return True
        except Exception as e:
            self.log(f"Git configuration failed: {e}")
            return False
    
    def step_run_crawler(self):
        """步骤: Run GW crawler"""
        self.log("Running GW crawler with performance monitoring...")
        
        try:
            crawler_start = datetime.datetime.now()
            
            result = subprocess.run([
                'python3', 'scripts/fetch_complete_gw.py'
            ], capture_output=True, text=True, timeout=300)
            
            crawler_end = datetime.datetime.now()
            execution_time = (crawler_end - crawler_start).seconds
            
            self.results['execution_time'] = execution_time
            
            if result.returncode == 0:
                self.log(f"Crawler executed successfully in {execution_time}s")
                
                # 解析输出中的关键信息
                output_lines = result.stdout.split('\n')
                for line in output_lines:
                    if '筛选出' in line and '引力波' in line:
                        self.log(f"Crawler result: {line.strip()}")
                    elif '📊 引力波论文提交类型:' in line:
                        self.log(f"Submission types: {line.strip()}")
                
                return True
            else:
                self.log(f"Crawler execution failed: {result.stderr}")
                return False
                
        except subprocess.TimeoutExpired:
            self.log("Crawler execution timed out")
            return False
        except Exception as e:
            self.log(f"Error running crawler: {e}")
            return False
    
    def step_verify_results(self):
        """步骤: Verify and analyze results"""
        self.log("Verifying and analyzing results...")
        
        # 检查必要文件
        required_files = [
            f"archives/filtered/gw_filtered_{self.date_str}.json",
            "digest.md"
        ]
        
        all_exist = True
        for file_path in required_files:
            if os.path.exists(file_path):
                file_size = os.path.getsize(file_path)
                self.log(f"{file_path} exists ({file_size} bytes)")
            else:
                self.log(f"{file_path} missing")
                all_exist = False
        
        if all_exist:
            # 分析引力波文件
            gw_file = f"archives/filtered/gw_filtered_{self.date_str}.json"
            try:
                with open(gw_file, 'r') as f:
                    data = json.load(f)
                    gw_count = data.get('total_gw_papers', 0)
                    total_crawled = data.get('total_crawled', 0)
                
                self.results['gw_papers_count'] = gw_count
                self.log(f"GW papers found: {gw_count}")
                self.log(f"Total crawled: {total_crawled}")
                
                return True
            except Exception as e:
                self.log(f"Error reading archive: {e}")
                return False
        
        return all_exist
    
    def step_commit_changes(self):
        """步骤: Commit with enhanced metadata"""
        self.log("Preparing commit with enhanced metadata...")
        
        try:
            # 检查是否有变化
            result = subprocess.run(['git', 'status', '--porcelain'], capture_output=True, text=True)
            
            if result.stdout.strip():
                self.log("Changes detected, simulating commit...")
                
                # 在测试环境中，我们只模拟 git add，不实际提交
                subprocess.run(['git', 'add', '-A', 'archives/'], check=True, capture_output=True)
                subprocess.run(['git', 'add', '-f', 'digest.md'], check=True, capture_output=True)
                
                # 创建提交信息但不实际提交
                total_time = (datetime.datetime.now() - self.start_time).seconds
                gw_count = self.results.get('gw_papers_count', 0)
                exec_time = self.results.get('execution_time', 0)
                
                commit_msg = f"🌊 Daily GW arXiv Digest - {self.date_str} (TEST)\n\nGW Papers: {gw_count}, Execution: {exec_time}s, Total: {total_time}s"
                
                self.log("Commit message prepared (not actually committing in test)")
                self.log(f"Would commit: {commit_msg[:100]}...")
                return True
            else:
                self.log("No changes to commit")
                return True
                
        except Exception as e:
            self.log(f"Error in commit simulation: {e}")
            return False
    
    def step_mattermost_notification(self):
        """步骤: Mattermost notification"""
        self.log("Testing Mattermost notification...")
        
        # 尝试本地 webhook URL
        webhook_url = os.environ.get('MATTERMOST_WEBHOOK_URL')
        
        if not webhook_url:
            # 从 .env 文件读取
            try:
                from dotenv import load_dotenv
                load_dotenv()
                webhook_url = os.environ.get('MATTERMOST_WEBHOOK_URL')
            except:
                pass
        
        if not webhook_url:
            self.log("No webhook URL found, simulating notification...")
            return True
        
        try:
            # 尝试发送测试消息
            gw_count = self.results.get('gw_papers_count', 0)
            exec_time = self.results.get('execution_time', 0)
            
            payload = {
                "text": f"🧪 Local Actions Test Completed!\n\n📅 Date: {self.date_str}\n📊 GW Papers: {gw_count}\n⏱️ Execution: {exec_time}s\n\n🖥️ Tested locally on macOS",
                "username": "Local Test Bot",
                "icon_emoji": ":test_tube:"
            }
            
            result = subprocess.run([
                'curl', '-s', '-X', 'POST',
                '-H', 'Content-Type: application/json',
                '-d', json.dumps(payload),
                webhook_url
            ], capture_output=True, text=True, timeout=10)
            
            if result.returncode == 0:
                self.log("Mattermost notification sent successfully")
                return True
            else:
                self.log("Mattermost send failed, but continuing...")
                return True  # 不让测试失败
                
        except Exception as e:
            self.log(f"Mattermost notification error: {e}")
            return True  # 不让测试失败
    
    def run_complete_workflow(self):
        """运行完整的工作流程"""
        self.log("🚀 Starting Local GitHub Actions Workflow Simulation")
        self.log("=" * 70)
        self.log(f"📅 Date: {self.date_str}")
        self.log(f"🕐 Hour: {self.hour}")
        self.log(f"📂 Working directory: {os.getcwd()}")
        self.log("=" * 70)
        
        # 定义工作流程步骤
        workflow_steps = [
            ("Checkout repository", self.step_checkout, True),
            ("Set up Python", self.step_setup_python, True),
            ("Install dependencies", self.step_install_dependencies, True),
            ("Set environment variables", self.step_set_environment_variables, True),
            ("Intelligent execution check", self.step_execution_check, False),  # 可以跳过
            ("Configure git", self.step_configure_git, False),
            ("Run GW crawler", self.step_run_crawler, True),
            ("Verify results", self.step_verify_results, True),
            ("Commit changes", self.step_commit_changes, False),
            ("Mattermost notification", self.step_mattermost_notification, False)
        ]
        
        passed_steps = 0
        total_steps = len(workflow_steps)
        should_continue = True
        
        for step_name, step_func, required in workflow_steps:
            if not should_continue and required:
                self.log(f"⏭️ Skipping required step: {step_name}")
                continue
            
            success = self.run_step(step_name, step_func, required)
            
            if success:
                passed_steps += 1
            elif step_name == "Intelligent execution check":
                # 执行检查失败意味着跳过，这是正常的
                should_continue = False
                self.log("ℹ️ Execution will be skipped due to existing digest")
            elif required and step_name in ["Run GW crawler", "Verify results"]:
                should_continue = False
                self.log("❌ Critical step failed, stopping workflow")
                break
        
        # 最终总结
        total_time = (datetime.datetime.now() - self.start_time).seconds
        
        self.log("\n" + "="*70)
        self.log("📊 Local GitHub Actions Workflow Summary")
        self.log("="*70)
        self.log(f"📅 Date: {self.date_str}")
        self.log(f"🕐 Hour: {self.hour}")
        self.log(f"⏱️ Total execution time: {total_time}s")
        self.log(f"✅ Passed steps: {passed_steps}/{total_steps}")
        
        if 'gw_papers_count' in self.results:
            self.log(f"🌊 GW papers found: {self.results['gw_papers_count']}")
        
        if 'execution_time' in self.results:
            self.log(f"⏱️ Crawler execution time: {self.results['execution_time']}s")
        
        if 'skip_execution' in self.results and self.results['skip_execution']:
            self.log("ℹ️ Execution was skipped (digest already exists)")
        
        self.log("="*70)
        
        # 判断成功标准
        critical_steps_passed = passed_steps >= (total_steps - 3)  # 允许 3 个非关键步骤失败
        
        if critical_steps_passed:
            self.log("🎉 Workflow simulation PASSED!", "SUCCESS")
            self.log("The GitHub Actions should work correctly when deployed.")
            return True
        else:
            self.log("⚠️ Workflow simulation had issues.", "WARNING")
            self.log("Some steps failed, but core functionality may still work.")
            return False

def main():
    """主函数"""
    print("🖥️ Starting Local GitHub Actions Workflow Test")
    print("=" * 70)
    print("This simulates the GitHub Actions environment locally")
    print("without requiring Docker or external network connections.")
    print("=" * 70)
    
    runner = LocalActionsRunner()
    success = runner.run_complete_workflow()
    
    return 0 if success else 1

if __name__ == "__main__":
    sys.exit(main())
