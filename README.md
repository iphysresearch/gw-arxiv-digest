# GW arXiv Digest - 引力波论文自动摘要

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Status](https://img.shields.io/badge/Status-Active-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

自动从 arXiv 网页爬取引力波相关论文，生成摘要并发送到 Mattermost。

## 🚀 特性

- **网页爬虫**: 直接从 arXiv 网页获取最新论文，无需 API 限制
- **智能筛选**: 先检查 "wave" 关键词，再确认引力波相关性
- **完整覆盖**: 
  - GR-QC: ~47 篇论文/天
  - Astro-Ph: ~150 篇论文/天（6个子类别）
- **自动存档**: 本地 JSON 存档，支持历史数据查询
- **Mattermost 集成**: 自动格式化并发送摘要消息

## 📊 爬取目标

| 类别 | URL | 预期数量 | 说明 |
|------|-----|----------|------|
| GR-QC | https://arxiv.org/list/gr-qc/new | ~47 篇 | 广义相对论和量子宇宙学 |
| Astro-Ph | 各子类别 /new 页面 | ~150 篇 | 天体物理学（6个子类别） |

## 🛠️ 快速开始

### 1. 环境准备

```bash
# 克隆仓库
git clone https://github.com/your-repo/gw-arxiv-digest.git
cd gw-arxiv-digest

# 检查项目状态
make status

# 安装依赖
make install
```

### 2. 基础测试

```bash
# 测试网页爬虫数量验证
make test-crawler

# 测试完整GW爬虫系统
make test-complete-gw

# 查看生成的存档
make view-archive
```

### 3. Mattermost 配置（可选）

创建 `.env` 文件：
```bash
MATTERMOST_WEBHOOK_URL=https://your-mattermost.com/hooks/xxx
ARXIV_MAX_RESULTS=300
ENABLE_ARCHIVE=true
```

测试 Mattermost 集成：
```bash
make test-webhook
make preview-mattermost
```

## 📋 主要命令

### 基础操作
```bash
make              # 运行完整测试流程
make test         # 测试主爬虫系统  
make test-crawler # 验证爬取数量（47+150篇）
make status       # 检查项目状态
```

### 存档管理
```bash
make view-archive     # 查看存档统计
make update-archives  # 强制更新存档文件
```

### Mattermost 集成
```bash
make test-webhook       # 测试webhook
make send-to-mattermost # 发送摘要到Mattermost
```

### 清理操作
```bash
make clean-temp    # 清理临时文件
make clean         # 清理生成文件（保留存档）
make clean-all     # 清理所有文件包括存档
```

## 📁 项目结构
