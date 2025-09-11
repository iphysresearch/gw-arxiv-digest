#!/bin/bash
# 使用 act 工具在本地测试 GitHub Actions

echo "🎭 Starting local GitHub Actions test with act"
echo "=============================================="

# 检查必要工具
if ! command -v act &> /dev/null; then
    echo "❌ act not installed. Install with: brew install act"
    exit 1
fi

if ! docker info &> /dev/null; then
    echo "❌ Docker not running. Please start Docker Desktop"
    exit 1
fi

echo "✅ Prerequisites check passed"

# 创建临时的 secrets 文件
SECRETS_FILE=".secrets"
cat > "$SECRETS_FILE" << EOF
MATTERMOST_WEBHOOK_URL=http://host.docker.internal:8080/hooks/test
GITHUB_TOKEN=test-token-for-local
EOF

echo "📝 Created temporary secrets file"

# 创建 act 配置文件
ACT_CONFIG=".actrc"
cat > "$ACT_CONFIG" << EOF
--container-architecture linux/amd64
--secret-file .secrets
--env ENABLE_ARCHIVE=true
--env ARCHIVE_DIR=archives/complete
EOF

echo "⚙️ Created act configuration"

# 运行主要的 workflow
echo ""
echo "🚀 Testing main workflow (arxiv-digest.yml)..."
echo "=============================================="

act workflow_dispatch \
    -W .github/workflows/arxiv-digest.yml \
    --secret-file "$SECRETS_FILE" \
    --env ENABLE_ARCHIVE=true \
    --env ARCHIVE_DIR=archives/complete \
    --verbose

MAIN_RESULT=$?

# 运行健康检查 workflow
echo ""
echo "🏥 Testing health check workflow..."
echo "=================================="

act workflow_dispatch \
    -W .github/workflows/health-check.yml \
    --secret-file "$SECRETS_FILE" \
    --verbose

HEALTH_RESULT=$?

# 清理
echo ""
echo "🧹 Cleaning up..."
rm -f "$SECRETS_FILE" "$ACT_CONFIG"

# 总结结果
echo ""
echo "📊 Local GitHub Actions Test Results"
echo "===================================="

if [ $MAIN_RESULT -eq 0 ]; then
    echo "✅ Main workflow (arxiv-digest.yml): PASSED"
else
    echo "❌ Main workflow (arxiv-digest.yml): FAILED"
fi

if [ $HEALTH_RESULT -eq 0 ]; then
    echo "✅ Health check workflow: PASSED"
else
    echo "❌ Health check workflow: FAILED"
fi

if [ $MAIN_RESULT -eq 0 ] && [ $HEALTH_RESULT -eq 0 ]; then
    echo ""
    echo "🎉 All GitHub Actions tests passed!"
    echo "The workflows should work correctly when deployed."
    exit 0
else
    echo ""
    echo "⚠️ Some tests failed. Check the output above for details."
    exit 1
fi
