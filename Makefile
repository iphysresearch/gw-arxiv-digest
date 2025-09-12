.PHONY: all install test test-crawler test-complete-gw test-webhook check-env clean clean-temp clean-all clean-scripts help

# Default target - run basic tests
all: check-env install test

# Install Python dependencies
install:
	@echo "📦 Installing Python dependencies..."
	pip install -r requirements.txt
	@echo "✅ Dependencies installed"

# Check local environment and tools
check-env:
	@echo "🔍 Checking local environment..."
	@python --version || (echo "❌ Python not found" && exit 1)
	@pip --version || (echo "❌ pip not found" && exit 1)
	@echo "✅ Python environment OK"

# Main test - Test complete GW crawler system
test: test-complete-gw

# Test comprehensive web crawler system
test-crawler:
	@echo "🕷️ Testing comprehensive web crawler system..."
	python comprehensive_crawler_test.py
	@if [ -f crawler_test_report_*.md ]; then \
		echo "📄 Test report generated:"; \
		ls -la crawler_test_report_*.md; \
	fi

# Test complete system with self-verification and classified archives
test-system-complete:
	@echo "🔧 Testing complete system with all features..."
	@echo "📋 This includes: self-verification, classified archives, and target validation"
	python test_system_complete.py
	@if [ $$? -eq 0 ]; then \
		echo ""; \
		echo "✅ Complete system test passed!"; \
		echo "🎯 All key features verified:"; \
		echo "  - Web crawler self-verification"; \
		echo "  - Classified archive creation"; \
		echo "  - Crawl target validation"; \
	else \
		echo ""; \
		echo "⚠️ System test failed - check output above"; \
	fi

# Test complete GW crawler with self-verification (main production script)
test-complete-gw:
	@echo "🌊 Testing complete GW web crawler with self-verification..."
	@echo "📡 Target: gr-qc (~47 papers) + astro-ph (~150 papers)"
	@echo "🔍 Will verify against page source: <div class=\"paging\">Total of XX entries</div>"
	@echo ""
	python scripts/fetch_complete_gw.py
	@if [ -f digest.md ]; then \
		echo ""; \
		echo "✅ Complete GW digest generated successfully"; \
		echo "📄 Digest preview:"; \
		head -15 digest.md; \
		echo "..."; \
		echo "📊 Digest stats: $$(wc -l < digest.md) lines"; \
		echo ""; \
		echo "📁 Archive files created:"; \
		find archives -name "*$$(date +%Y-%m-%d)*" -type f 2>/dev/null | while read file; do \
			echo "  - $$file ($$(stat -f%z "$$file" 2>/dev/null || stat -c%s "$$file" 2>/dev/null || echo "unknown") bytes)"; \
		done; \
		echo ""; \
		$(MAKE) verify-archive-quality; \
	else \
		echo "❌ digest.md not generated"; \
		exit 1; \
	fi
	@if [ -f mattermost_preview.md ]; then \
		echo "📱 Mattermost preview: $$(wc -c < mattermost_preview.md) characters"; \
	fi

# Test webhook functionality
test-webhook:
	@echo "📡 Testing Mattermost webhook..."
	@if [ -f .env ]; then \
		echo "✅ 检测到 .env 文件"; \
		WEBHOOK_URL=$$(grep "^MATTERMOST_WEBHOOK_URL=" .env | cut -d'=' -f2- | tr -d '"'); \
		if [ -z "$$WEBHOOK_URL" ]; then \
			echo "❌ MATTERMOST_WEBHOOK_URL not found in .env file"; \
			exit 1; \
		else \
			echo "Sending test message to Mattermost..."; \
			curl -s -X POST -H 'Content-Type: application/json' \
				-d '{"text": "🧪 Test from gw-arxiv-digest Makefile - Web crawler system operational! All self-verification passed ✅", "username": "GW arXiv Bot", "icon_emoji": ":telescope:"}' \
				$$WEBHOOK_URL && echo "✅ Webhook test sent" || echo "❌ Webhook test failed"; \
		fi; \
	else \
		echo "❌ .env file not found"; \
		echo "💡 Create .env file with MATTERMOST_WEBHOOK_URL"; \
		exit 1; \
	fi

# Generate and preview Mattermost message format
preview-mattermost:
	@echo "📱 生成 Mattermost 消息预览..."
	python scripts/fetch_complete_gw.py
	@if [ -f mattermost_preview.md ]; then \
		echo "✅ Mattermost 预览已生成"; \
		echo ""; \
		echo "📄 === Mattermost 消息预览 ==="; \
		cat mattermost_preview.md; \
		echo ""; \
		echo "📊 消息长度: $$(wc -c < mattermost_preview.md) 字符"; \
	else \
		echo "❌ mattermost_preview.md 未生成"; \
		exit 1; \
	fi

# Send complete GW digest to Mattermost
send-to-mattermost:
	@echo "🌊 发送完整引力波 digest 到 Mattermost..."
	@if [ -f .env ]; then \
		python scripts/send_complete_gw.py; \
		echo "🧹 自动清理临时文件..."; \
		$(MAKE) clean-temp; \
	else \
		echo "❌ .env file not found"; \
		exit 1; \
	fi

# View archive index and statistics with verification info
view-archive:
	@echo "📚 查看存档索引和统计..."
	@if [ -d archives ]; then \
		echo "=== 存档目录结构 ==="; \
		find archives -name "*.json" -type f | head -10; \
		echo ""; \
		echo "=== 最新存档统计 ==="; \
		if [ -f archives/filtered/gw_filtered_$$(date +%Y-%m-%d).json ]; then \
			echo "📄 今日引力波筛选存档: archives/filtered/gw_filtered_$$(date +%Y-%m-%d).json"; \
			python -c "import json; data=json.load(open('archives/filtered/gw_filtered_$$(date +%Y-%m-%d).json')); print(f'📊 引力波论文: {data.get(\"summary\", {}).get(\"total_gw_papers\", 0)} 篇'); print(f'📊 总爬取: {data.get(\"summary\", {}).get(\"total_crawled\", 0)} 篇'); verification=data.get('crawl_verification', {}); print(f'🔍 验证状态: {\"✅ 通过\" if verification.get(\"verification_passed\") else \"⚠️ 异常\"}'); print(f'🔍 期望/实际: {verification.get(\"total_expected\", 0)}/{verification.get(\"total_actual\", 0)} 篇')"; \
		else \
			echo "📄 暂无今日存档"; \
		fi; \
		echo ""; \
		echo "=== 分类存档文件 ==="; \
		for file in archives/complete/gr_qc_$$(date +%Y-%m-%d).json archives/complete/astro_ph_$$(date +%Y-%m-%d).json; do \
			if [ -f "$$file" ]; then \
				echo "📂 $$file"; \
				python -c "import json; data=json.load(open('$$file')); print(f'   📊 {data.get(\"category\", \"Unknown\")}: {data.get(\"total_papers\", 0)} 篇 (引力波相关: {data.get(\"gw_related_papers\", 0)} 篇)')"; \
			fi; \
		done; \
		echo ""; \
		echo "=== 存档文件数量 ==="; \
		echo "Complete (原始): $$(find archives/complete -name "*.json" -type f | wc -l) 个文件"; \
		echo "Filtered (引力波): $$(find archives/filtered -name "*.json" -type f | wc -l) 个文件"; \
		echo "Total size: $$(du -sh archives 2>/dev/null | cut -f1)"; \
	else \
		echo "❌ 存档目录不存在"; \
	fi

# Verify archive quality and completeness
verify-archive-quality:
	@echo "🔍 验证存档质量和完整性..."
	@date_str=$$(date +%Y-%m-%d); \
	filtered_file="archives/filtered/gw_filtered_$$date_str.json"; \
	gr_qc_file="archives/complete/gr_qc_$$date_str.json"; \
	astro_file="archives/complete/astro_ph_$$date_str.json"; \
	if [ -f "$$filtered_file" ]; then \
		echo "✅ 引力波筛选存档存在: $$filtered_file"; \
		python -c "import json; data=json.load(open('$$filtered_file')); verification=data.get('crawl_verification', {}); details=verification.get('category_details', []); print('📊 详细验证结果:'); [print(f'   {d.get(\"category\", \"?\")}: {\"✅\" if d.get(\"verification_passed\") else \"⚠️\"} {d.get(\"actual_crawled\", 0)}/{d.get(\"expected_total\", 0)} 篇') for d in details if d.get('expected_total', 0) > 0]; summary = data.get('summary', {}); print(f'🌊 引力波论文: {summary.get(\"total_gw_papers\", 0)} 篇'); papers = data.get('papers', []); submission_types = {}; [submission_types.update({p.get('submission_info', {}).get('type', 'new'): submission_types.get(p.get('submission_info', {}).get('type', 'new'), 0) + 1}) for p in papers]; print(f'📊 提交类型: New={submission_types.get(\"new\", 0)}, Cross-list={submission_types.get(\"cross-list\", 0)}, Replaced={submission_types.get(\"replaced\", 0)}')"; \
	else \
		echo "❌ 引力波筛选存档不存在: $$filtered_file"; \
	fi; \
	if [ -f "$$gr_qc_file" ]; then \
		echo "✅ GR-QC 分类存档存在: $$gr_qc_file"; \
	else \
		echo "⚠️ GR-QC 分类存档不存在: $$gr_qc_file"; \
	fi; \
	if [ -f "$$astro_file" ]; then \
		echo "✅ Astro-Ph 分类存档存在: $$astro_file"; \
	else \
		echo "⚠️ Astro-Ph 分类存档不存在: $$astro_file"; \
	fi

# Verify crawling accuracy against expected targets
verify-crawl-targets:
	@echo "🎯 验证爬取数量是否达到目标..."
	@echo "目标: GR-QC ~47篇, Astro-Ph子类别各自验证通过即可"
	@date_str=$$(date +%Y-%m-%d); \
	filtered_file="archives/filtered/gw_filtered_$$date_str.json"; \
	if [ -f "$$filtered_file" ]; then \
		python -c "import json; data=json.load(open('$$filtered_file')); verification=data.get('crawl_verification', {}); details=verification.get('category_details', []); gr_qc_count=sum(d.get('actual_crawled', 0) for d in details if d.get('category', '') == 'gr-qc'); print(f'📊 GR-QC: {gr_qc_count} 篇 (目标: 47篇) {\"✅\" if 35 <= gr_qc_count <= 60 else \"⚠️\"}'); astro_details = [d for d in details if d.get('category', '').startswith('astro-ph')]; astro_passed = sum(1 for d in astro_details if d.get('verification_passed', False)); astro_total = len(astro_details); print(f'📊 Astro-Ph子类别验证: {astro_passed}/{astro_total} 个通过 {\"✅\" if astro_passed == astro_total else \"⚠️\"}'); [print(f'   {d.get(\"category\", \"?\")}: {d.get(\"actual_crawled\", 0)}/{d.get(\"expected_total\", 0)} 篇 {\"✅\" if d.get(\"verification_passed\") else \"⚠️\"}') for d in astro_details]; total_expected = verification.get('total_expected', 0); total_actual = verification.get('total_actual', 0); print(f'📊 页面验证: {\"✅ 通过\" if verification.get(\"verification_passed\") else \"⚠️ 异常\"} ({total_actual}/{total_expected} 篇)'); summary = data.get('summary', {}); print(f'🌊 引力波筛选: {summary.get(\"total_gw_papers\", 0)} 篇')"; \
	else \
		echo "❌ 找不到今日筛选存档文件，请先运行 make test-complete-gw"; \
		exit 1; \
	fi

# Update archives (force refresh)
update-archives:
	@echo "🔄 更新本地存档文件..."
	@echo "⚠️  这将覆盖今日的存档文件"
	@read -p "继续吗？[y/N] " confirm && [ "$$confirm" = "y" ] || exit 1
	python scripts/fetch_complete_gw.py
	@echo "✅ 存档文件已更新"
	$(MAKE) view-archive

# Clean up temporary files only (preserve archives)
clean-temp:
	@echo "🧹 清理临时文件..."
	rm -f digest.md mattermost_preview.md
	rm -f crawler_test_report_*.md
	rm -f *.py.tmp
	rm -rf scripts/__pycache__/ __pycache__/
	@echo "✅ 临时文件已清理 (存档文件保留)"

# Clean up generated files (preserve archives)
clean:
	@echo "🧹 清理生成的文件..."
	python scripts/cleanup.py 2>/dev/null || $(MAKE) clean-temp
	@echo "✅ 生成文件已清理 (存档文件保留)"

# Clean everything including archives
clean-all:
	@echo "🧹 清理所有文件和存档..."
	@echo "⚠️  这将删除所有存档数据！"
	@read -p "确定要继续吗？[y/N] " confirm && [ "$$confirm" = "y" ] || exit 1
	rm -f digest.md mattermost_preview.md crawler_test_report_*.md
	rm -f quick_test.py test_crawler_simple.py
	rm -rf archives/complete/* archives/filtered/* archives/arxiv/*
	rm -rf scripts/__pycache__/ __pycache__/
	@echo "✅ 所有文件已清理"

# Clean up obsolete scripts
clean-scripts:
	@echo "🧹 清理过时和重复的脚本文件..."
	@echo "以下文件将被删除:"
	@echo "  - scripts/fetch_arxiv_enhanced.py (使用旧 arxiv 库)"
	@echo "  - scripts/fetch_gw_papers.py (功能重复)"
	@echo "  - scripts/test_local.py (使用旧 arxiv 库)"
	@echo "  - scripts/test_web_scraper.py (功能重复)" 
	@echo "  - scripts/send_to_mattermost.py (依赖旧脚本)"
	@echo "  - scripts/send_gw_digest.py (依赖旧脚本)"
	@echo "  - scripts/lv_web_scraper.py (重复文件)"
	@echo "  - quick_test.py (临时文件)"
	@echo "  - test_crawler_simple.py (临时文件)"
	@echo ""
	@read -p "确定要删除这些文件吗？[y/N] " confirm && [ "$$confirm" = "y" ] || exit 1
	rm -f scripts/fetch_arxiv_enhanced.py
	rm -f scripts/fetch_gw_papers.py  
	rm -f scripts/test_local.py
	rm -f scripts/test_web_scraper.py
	rm -f scripts/send_to_mattermost.py
	rm -f scripts/send_gw_digest.py
	rm -f scripts/lv_web_scraper.py
	rm -f quick_test.py
	rm -f test_crawler_simple.py
	@echo "✅ 过时脚本已清理"
	@echo "📋 剩余的核心脚本文件:"
	@ls -la scripts/

# Show project status
status:
	@echo "📊 项目状态检查..."
	@echo ""
	@echo "🔧 核心组件:"
	@[ -f scripts/arxiv_web_scraper.py ] && echo "  ✅ 网页爬虫模块" || echo "  ❌ 网页爬虫模块"
	@[ -f scripts/fetch_complete_gw.py ] && echo "  ✅ 主爬取脚本" || echo "  ❌ 主爬取脚本"
	@[ -f scripts/send_complete_gw.py ] && echo "  ✅ Mattermost 发送脚本" || echo "  ❌ Mattermost 发送脚本"
	@[ -f test_system_complete.py ] && echo "  ✅ 测试脚本" || echo "  ❌ 测试脚本"
	@echo ""
	@echo "📁 存档状态:"
	@[ -d archives/complete ] && echo "  ✅ 完整存档目录 ($$(find archives/complete -name "*.json" | wc -l) 个文件)" || echo "  ❌ 完整存档目录"
	@echo ""
	@echo "📦 依赖检查:"
	@python -c "import requests; print('  ✅ requests')" 2>/dev/null || echo "  ❌ requests"
	@python -c "import bs4; print('  ✅ beautifulsoup4')" 2>/dev/null || echo "  ❌ beautifulsoup4"
	@python -c "from dotenv import load_dotenv; print('  ✅ python-dotenv')" 2>/dev/null || echo "  ❌ python-dotenv"
	@echo ""
	@echo "⚙️  配置文件:"
	@[ -f .env ] && echo "  ✅ .env 文件存在" || echo "  ⚠️  .env 文件不存在 (Mattermost 功能不可用)"

# Show help
help:
	@echo "🚀 GW arXiv Digest - 网页爬虫自检版本"
	@echo "=========================================="
	@echo ""
	@echo "📋 基础命令:"
	@echo "  make              - 运行基础测试 (check-env + install + test)"
	@echo "  make install      - 安装 Python 依赖"
	@echo "  make test         - 运行主要测试 (等同于 test-complete-gw)"
	@echo "  make test-crawler - 测试网页爬虫系统和数量验证"
	@echo "  make test-complete-gw - 测试完整GW爬虫 (包含自检功能)"
	@echo "  make test-system-complete - 测试完整系统 (包含所有功能验证)"
	@echo "  make status       - 检查项目状态和组件"
	@echo ""
	@echo "🔍 验证和自检:"
	@echo "  make verify-archive-quality - 验证存档文件质量和完整性"
	@echo "  make verify-crawl-targets   - 验证爬取数量是否达到目标"
	@echo "  make view-archive          - 查看存档统计 (包含验证信息)"
	@echo ""
	@echo "📊 存档管理:"
	@echo "  make update-archives - 强制更新本地存档文件"
	@echo ""
	@echo "📡 Mattermost 集成:"
	@echo "  make test-webhook - 测试 Mattermost webhook"
	@echo "  make preview-mattermost - 生成消息预览"
	@echo "  make send-to-mattermost - 发送GW digest到Mattermost"
	@echo ""
	@echo "🧹 清理命令:"
	@echo "  make clean-temp   - 清理临时文件 (保留存档)"
	@echo "  make clean        - 清理生成文件 (保留存档)"
	@echo "  make clean-all    - 清理所有文件包括存档 ⚠️"
	@echo "  make clean-scripts - 清理过时和重复的脚本文件 ⚠️"
	@echo ""
	@echo "🔧 系统检查:"
	@echo "  make check-env    - 检查本地环境"
	@echo "  make help         - 显示此帮助信息"
	@echo ""
	@echo "🎯 自检功能说明:"
	@echo "  • 解析页面源代码中的总数信息: <div class=\"paging\">Total of XX entries</div>"
	@echo "  • 验证实际爬取数量与页面显示数量的匹配度 (容差±5篇)"
	@echo "  • 按类别分类存档: gr_qc_YYYY-MM-DD.json, astro_ph_YYYY-MM-DD.json"
	@echo "  • 包含详细的爬取验证统计信息"
	@echo ""
	@echo "💡 推荐工作流:"
	@echo "  1. make status                 # 检查项目状态"
	@echo "  2. make install                # 安装依赖"  
	@echo "  3. make test-system-complete   # 运行完整系统测试 (推荐)"
	@echo "  4. make verify-crawl-targets   # 验证爬取目标达成情况"
	@echo "  5. make view-archive           # 查看详细存档统计"
	@echo ""
	@echo "🚀 快速测试:"
	@echo "  make test-complete-gw          # 仅测试GW爬虫 (快速)"
	@echo ""
	@echo "📚 目标和验证:"
	@echo "  • GR-QC: ~47篇 (验证范围: 35-60篇)"
	@echo "  • Astro-Ph: ~150篇 (验证范围: 120-200篇)"  
	@echo "  • 自动验证页面总数与爬取数量的一致性"
	@echo ""
	@echo "🎭 GitHub Actions 测试:"
	@echo "  make test-actions-local        # 本地 Actions 模拟 (推荐)"
	@echo "  make test-pr-workflow          # 测试 PR 工作流程"
	@echo "  make test-actions-simple       # 简化 Actions 测试"
	@echo "  make quick-docker-test         # 快速 Docker 测试"
	@echo ""
	@echo "🐳 Docker 测试环境 (可选):"
	@echo "  make docker-up                 # 启动 Docker 测试环境"
	@echo "  make docker-test               # 在 Docker 中测试 Actions"
	@echo "  make docker-shell              # 进入 Docker 测试环境"
	@echo "  make docker-down               # 停止 Docker 测试环境"

# Docker 本地 Actions 测试环境
docker-build:
	@echo "🐳 Building Docker test image..."
	@if ! docker info > /dev/null 2>&1; then \
		echo "❌ Docker not running. Please start Docker Desktop"; \
		exit 1; \
	fi
	docker build -f Dockerfile.test -t gw-arxiv-test .
	@echo "✅ Docker test image built"

docker-up: docker-build
	@echo "🐳 Starting Docker test environment..."
	@echo "📦 Starting containers..."
	docker-compose -f docker-compose.test.yml up -d
	@echo "✅ Docker test environment started"
	@echo "🌐 Mattermost mock available at: http://localhost:8080"
	@echo "⏳ Waiting for containers to be ready..."
	@sleep 5

docker-down:
	@echo "🐳 Stopping Docker test environment..."
	docker-compose -f docker-compose.test.yml down
	docker rmi gw-arxiv-test 2>/dev/null || true
	@echo "✅ Docker test environment stopped"

docker-test:
	@echo "🐳 Running Actions simulation in Docker..."
	@if ! docker info > /dev/null 2>&1; then \
		echo "❌ Docker not running. Run 'make docker-up' first"; \
		exit 1; \
	fi
	@if ! docker ps | grep gw-arxiv-actions-test > /dev/null; then \
		echo "❌ Test container not running. Run 'make docker-up' first"; \
		exit 1; \
	fi
	@echo "🚀 Executing GitHub Actions workflow simulation..."
	docker exec gw-arxiv-actions-test python3 scripts/simulate_actions.py

docker-shell:
	@echo "🐳 Opening shell in Docker test environment..."
	@if ! docker ps | grep gw-arxiv-actions-test > /dev/null; then \
		echo "❌ Test container not running. Run 'make docker-up' first"; \
		exit 1; \
	fi
	docker exec -it gw-arxiv-actions-test bash

# 本地 Actions 测试（推荐，不需要 Docker）
test-actions-local:
	@echo "🖥️ Running local GitHub Actions simulation..."
	@echo "📋 This simulates the complete workflow locally"
	python3 scripts/local_actions_test.py

# 测试 PR 工作流程
test-pr-workflow:
	@echo "📋 Testing PR workflow logic..."
	@echo "🔍 This tests skip logic, PR creation, and auto-merge"
	python3 scripts/test_pr_workflow.py

# 简化的本地 Actions 测试
test-actions-simple:
	@echo "🎭 Running simple Actions simulation..."
	@echo "📋 This simulates the workflow steps without Docker"
	python3 scripts/test_actions_local.py

# 测试所有 Actions 功能（推荐）
test-actions-complete: docker-up
	@echo "🧪 Running complete Actions test suite..."
	@echo ""
	@echo "1. 🐳 Testing in Docker environment..."
	make docker-test
	@echo ""
	@echo "2. 🔍 Verifying results..."
	@if docker exec gw-arxiv-actions-test ls archives/filtered/ | grep gw_filtered > /dev/null; then \
		echo "✅ Archive files created successfully"; \
	else \
		echo "⚠️ Archive files not found"; \
	fi
	@echo ""
	@echo "3. 🌐 Testing Mattermost mock..."
	@curl -s http://localhost:8080 > /dev/null && echo "✅ Mattermost mock responsive" || echo "⚠️ Mattermost mock not responsive"
	@echo ""
	@echo "✅ Complete Actions test finished"
	make docker-down

# 快速 Docker 测试（一键测试）
quick-docker-test:
	@echo "⚡ Quick Docker Actions test..."
	make docker-up
	@sleep 3
	make docker-test
	make docker-down
