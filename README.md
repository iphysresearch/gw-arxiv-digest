# GW arXiv Digest - Gravitational Wave Paper Automated Digest

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Status](https://img.shields.io/badge/Status-Active-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

An automated system that crawls arXiv for gravitational wave related papers, generates comprehensive digests, and sends them to Mattermost channels.

## 🌊 Overview

GW arXiv Digest is a comprehensive web scraping system that automatically discovers, filters, and summarizes gravitational wave research papers from arXiv. The system performs intelligent filtering, self-verification of crawl accuracy, and provides automated integration with Mattermost for team notifications.

### Key Capabilities

- **Web-Based Crawling**: Direct scraping from arXiv web pages with no API limitations
- **Intelligent Filtering**: Two-stage filtering process using "wave" keywords and gravitational wave relevance detection
- **Self-Verification**: Automatic validation of crawl completeness against page source metadata
- **Comprehensive Coverage**: 
  - **GR-QC**: ~50 papers/day (General Relativity and Quantum Cosmology)
  - **Astro-Ph**: ~150 papers/day (Astrophysics across 6 subcategories)
- **Automated Archiving**: Local JSON archives with detailed metadata and verification statistics
- **Mattermost Integration**: Formatted digest delivery with automatic cleanup

## 🎯 Crawl Targets

| Category | URL Pattern | Expected Volume | Description |
|----------|-------------|-----------------|-------------|
| **GR-QC** | `https://arxiv.org/list/gr-qc/new` | ~50 papers | General Relativity and Quantum Cosmology |
| **Astro-Ph** | `https://arxiv.org/list/astro-ph.*/new` | ~150 papers | Astrophysics (6 subcategories) |

### Verification System
The system automatically validates crawl accuracy by:
- Parsing page source for total entry counts: `<div class="paging">Total of XX entries</div>`
- Comparing expected vs actual crawled papers (±5 paper tolerance)
- Generating detailed verification reports in archive files

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Internet connection for arXiv access
- Optional: Mattermost webhook for notifications

### Installation

```bash
# Clone the repository
git clone https://github.com/your-repo/gw-arxiv-digest.git
cd gw-arxiv-digest

# Check project status
make status

# Install dependencies
make install
```

### Basic Usage

```bash
# Run comprehensive system test
make test-system-complete

# Run main GW crawler (production)
make test-complete-gw

# View archive statistics
make view-archive

# Verify crawl targets achieved
make verify-crawl-targets
```

## ⚙️ Configuration

### Environment Setup

Create a `.env` file for optional configurations:

```bash
# Mattermost Integration (optional)
MATTERMOST_WEBHOOK_URL=https://your-mattermost.com/hooks/xxx

# Crawling Configuration
ARXIV_MAX_RESULTS=300
ENABLE_ARCHIVE=true

# Mattermost Formatting
MATTERMOST_MAX_PAPERS=100
```

### Archive Configuration

Archives are automatically created in:
- `archives/complete/` - Raw categorized papers (gr_qc_YYYY-MM-DD.json, astro_ph_YYYY-MM-DD.json)
- `archives/filtered/` - GW-filtered papers with verification data (gw_filtered_YYYY-MM-DD.json)

## 📋 Available Commands

### Core Operations
```bash
make              # Run basic test suite
make test         # Run main GW crawler test
make test-crawler # Test web crawler with quantity verification
make test-system-complete # Complete system test with all features
make status       # Check project health and components
```

### Verification & Quality Assurance
```bash
make verify-archive-quality   # Verify archive file integrity
make verify-crawl-targets     # Check if crawl targets are met
make view-archive             # Display archive statistics with verification info
```

### Mattermost Integration
```bash
make test-webhook           # Test Mattermost connectivity
make preview-mattermost     # Generate message preview
make send-to-mattermost     # Send GW digest to Mattermost
```

### Maintenance
```bash
make update-archives        # Force refresh archive files
make clean-temp            # Clean temporary files (preserve archives)
make clean                 # Clean generated files (preserve archives)  
make clean-all             # Clean everything including archives ⚠️
```

## 🏗️ Project Structure

```
gw-arxiv-digest/
├── scripts/                    # Core application modules
│   ├── arxiv_web_scraper.py   # Web scraping engine with self-verification
│   ├── fetch_complete_gw.py   # Main processing pipeline
│   ├── send_complete_gw.py    # Mattermost integration
│   └── cleanup.py             # Automated cleanup utilities
├── archives/                   # Data storage
│   ├── complete/              # Raw categorized papers by date
│   └── filtered/              # GW-filtered papers with metadata
├── test_system_complete.py     # Comprehensive test suite
├── Makefile                   # Automation and workflow management
├── requirements.txt           # Python dependencies
└── README.md                  # This documentation
```

### Key Components

#### `arxiv_web_scraper.py`
- Web-based arXiv crawler replacing API dependencies
- Built-in self-verification against page metadata
- Category-specific crawling with statistics tracking

#### `fetch_complete_gw.py`
- Main processing pipeline
- Intelligent GW paper filtering
- Archive management with detailed verification
- Digest generation for multiple output formats

#### `test_system_complete.py`
- Comprehensive validation suite
- Archive integrity verification
- Crawl accuracy validation
- System health monitoring

## 🔍 Self-Verification Features

The system includes robust self-verification capabilities:

### Crawl Verification
- **Page Source Parsing**: Extracts total entry counts from arXiv page HTML
- **Tolerance Checking**: Validates actual crawled papers against expected counts (±5 paper tolerance)
- **Category Breakdown**: Individual verification for each crawled category
- **Statistical Reporting**: Detailed verification statistics in archive files

### Archive Verification
```bash
# Check archive quality and completeness
make verify-archive-quality

# Verify crawl targets (GR-QC: 35-60 papers, Astro-Ph: all subcategories pass)
make verify-crawl-targets
```

### Verification Targets
- **GR-QC**: 35-60 papers (target: ~47)
- **Astro-Ph**: All subcategories must pass individual verification
- **Page Validation**: Automatic verification of total counts vs crawled papers

## 📊 Archive Format

### Filtered Archive (`gw_filtered_YYYY-MM-DD.json`)
```json
{
  "crawl_date": "2025-09-10",
  "summary": {
    "total_crawled": 197,
    "total_gw_papers": 15
  },
  "crawl_verification": {
    "verification_passed": true,
    "total_expected": 197,
    "total_actual": 197,
    "category_details": [...]
  },
  "papers": [...]
}
```

### Complete Archive (`gr_qc_YYYY-MM-DD.json`, `astro_ph_YYYY-MM-DD.json`)
```json
{
  "category": "gr-qc",
  "crawl_date": "2025-09-10",
  "total_papers": 47,
  "gw_related_papers": 12,
  "papers": [...],
  "verification": {...}
}
```

## 🧪 Testing

### Recommended Testing Workflow

1. **System Health Check**: `make status`
2. **Install Dependencies**: `make install`
3. **Complete System Test**: `make test-system-complete` (recommended)
4. **Verify Targets**: `make verify-crawl-targets`
5. **Review Archives**: `make view-archive`

### Quick Testing
```bash
# Fast GW crawler test only
make test-complete-gw
```

### Test Coverage
- ✅ Web crawler module import
- ✅ Single category crawling with self-verification
- ✅ Complete system pipeline
- ✅ Archive file structure validation
- ✅ Crawl target achievement verification

## 🚀 Production Deployment

### Automated Workflow
```bash
# 1. Run complete system test
make test-system-complete

# 2. Verify targets achieved  
make verify-crawl-targets

# 3. Send to Mattermost (if configured)
make send-to-mattermost

# 4. Automatic cleanup
# (handled by send-to-mattermost target)
```

### Mattermost Integration
With proper `.env` configuration, the system can automatically:
- Format papers into readable digest messages
- Send notifications to configured channels
- Clean up temporary files after sending
- Provide delivery confirmations

## 📈 Performance & Reliability

### Expected Performance
- **GR-QC Crawling**: 35-60 papers (~47 target)
- **Astro-Ph Crawling**: 120-200 papers (~150 target)
- **Processing Time**: ~2-5 minutes for complete crawl
- **Verification Accuracy**: >95% crawl completeness validation

### Error Handling
- Automatic retry mechanisms for failed requests
- Tolerance-based verification (±5 papers)
- Detailed error logging in verification reports
- Graceful degradation for partial crawl failures

## 🤝 Contributing

### Development Setup
1. Fork the repository
2. Create a feature branch
3. Install dependencies: `make install`
4. Run tests: `make test-system-complete`
5. Verify your changes don't break existing functionality

### Code Standards
- Follow existing Python code style
- Add tests for new features
- Update documentation for user-facing changes
- Ensure self-verification features work correctly

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- arXiv for providing open access to scientific papers
- The gravitational wave community for advancing the field
- Python community for excellent scraping and processing libraries

---

**Note**: This system is designed for research and educational purposes. Please respect arXiv's terms of service and implement appropriate rate limiting in production environments.