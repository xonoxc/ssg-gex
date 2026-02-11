# SSG-GEX: Modern Python Static Site Generator

[![Python Version](https://img.shields.io/badge/python-3.13+-blue.svg)](https://python.org)
[![PyPI Version](https://img.shields.io/pypi/v/ssg-gex.svg)](https://pypi.org/project/ssg-gex/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Type Checking: mypy](https://img.shields.io/badge/type%20checking-mypy-blue.svg)](http://mypy-lang.org/)
[![Test Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen.svg)](pytest --cov=src)
[![Tests](https://img.shields.io/badge/tests-passing-brightgreen.svg)](pytest)
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)]()

A clean, type-safe static site generator built with modern Python 3.13. SSG-GEX transforms your Markdown content into fast, secure websites using a node-based architecture that provides both simplicity and extensibility.

## ✨ Features

- **🔒 Type-Safe Architecture**: Built with comprehensive type annotations for reliability and IDE support
- **🌳 Node-Based Design**: Extensible HTML node system supporting complex content structures
- **📝 Rich Text Support**: Native support for plain text, bold, italic, code, links, and images
- **🔄 Markdown Processing**: Complete markdown to HTML conversion with block-level and inline formatting
- **🧪 Comprehensive Testing**: Full test coverage with pytest ensuring code quality (115 tests)
- **🐍 Modern Python**: Uses Python 3.13+ features for clean, maintainable code
- **⚡ Fast Builds**: Efficient processing with minimal overhead
- **🎯 Simple Deployment**: Generates static files ready for any web server

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/your-username/ssg-gex.git
cd ssg-gex

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -e .
```

### Basic Usage

```python
from src.utils.markdown_to_html_nodes import markdown_to_html_nodes

# Convert markdown to HTML
markdown_content = """
# Welcome

This is **bold** and _italic_ text with `code` examples.

- Item 1
- Item 2

> This is a quote
"""

html_node = markdown_to_html_nodes(markdown_content)
html_output = html_node.to_html()
print(html_output)
# Output: <div><h1>Welcome</h1><p>This is <b>bold</b> and <i>italic</i> text with <code>code</code> examples.</p><ul><li>Item 1</li><li>Item 2</li></ul><blockquote>This is a quote</blockquote></div>
```

### Build Your Site

```bash
# Build and serve the site
./main.sh          # Runs build.py + starts dev server on port 8888

# Build only
python src/main.py # Generate static files

# Run tests
pytest             # Run all tests
pytest --cov=src   # Run with coverage
```

## 🏗️ Architecture

SSG-GEX follows a clean, modular architecture:

```
ssg-gex/
├── src/                          # Main source code
│   ├── main.py                   # Entry point
│   ├── build.py                  # Build orchestration
│   ├── constants.py              # Path configurations
│   ├── errors/                   # Custom error handling
│   ├── generators/               # Page generation logic
│   ├── nodes/                    # HTML node architecture
│   │   ├── blocks/               # Block-level elements
│   │   ├── htmlnode.py           # Core HTML node
│   │   ├── leafnode.py           # Terminal nodes
│   │   ├── parentnode.py         # Container nodes
│   │   └── textnode.py           # Text content nodes
│   └── utils/                    # Utility functions
│       ├── files/                # File management
│       ├── markdown_to_html_nodes.py  # Core markdown conversion
│       ├── text_to_nodes.py      # Text parsing
│       └── extract_title.py      # Title extraction
├── content/                      # Source content (Markdown)
├── static/                       # Static assets
├── template.html                 # HTML template
├── main.sh                       # Build and serve script
└── pyproject.toml                # Project configuration
```

### Core Components

#### 🌳 Node Architecture
- **HTMLNode**: Base class for all HTML elements
- **LeafNode**: Terminal elements (no children)
- **ParentNode**: Container elements with children
- **TextNode**: Handles different text types (plain, bold, italic, code, links, images)

#### 🔄 Markdown Processing Pipeline
- **Block Detection**: Identifies paragraphs, headings, code blocks, quotes, lists
- **Inline Parsing**: Handles bold (`**text**`), italic (`_text_`), code (`` `text` ``), links, images
- **HTML Generation**: Converts parsed content to semantic HTML

#### 🏗️ Build System
- **Content Processing**: Recursively processes Markdown files
- **Template Injection**: Uses `{{ variable }}` syntax for templates
- **Static Asset Management**: Copies static files to output directory

## 📝 Supported Markdown Features

### Block Elements
- **Headings**: `# H1` through `###### H6`
- **Paragraphs**: Plain text separated by blank lines
- **Code Blocks**: Fenced with triple backticks ```
- **Quotes**: Lines starting with `>`
- **Unordered Lists**: Lines starting with `- `
- **Ordered Lists**: Lines starting with `1. `, `2. `, etc.

### Inline Formatting
- **Bold**: `**text**` → `<b>text</b>`
- **Italic**: `_text_` → `<i>text</i>`
- **Code**: `` `text` `` → `<code>text</code>`
- **Links**: `[text](url)` → `<a href="url">text</a>`
- **Images**: `[alt](src)` → `<img src="src" alt="alt">`

## 🧪 Testing

SSG-GEX emphasizes comprehensive testing with 115 tests covering:

```bash
# Run all tests
pytest

# Run tests with coverage
pytest --cov=src

# Run specific test file
pytest src/nodes/htmlnode_test.py -v

# Run markdown processing tests
pytest src/utils/markdown_to_html_nodes_test.py -v
```

### Test Coverage Areas
- Node architecture (HTMLNode, LeafNode, ParentNode, TextNode)
- Markdown parsing (blocks, inline formatting)
- Utility functions
- Page generation
- Edge case validation

## 📊 Current Status ✅

### Completed Features
- [x] Complete markdown to HTML conversion
- [x] All block-level elements support
- [x] All inline formatting support
- [x] Type-safe node architecture
- [x] Comprehensive test coverage (115 tests)
- [x] Template system with variable injection
- [x] Static asset management
- [x] Development server

## 🗺️ Roadmap

- [ ] CLI interface improvements
- [ ] Plugin architecture
- [ ] Asset optimization (CSS/JS minification)
- [ ] Live reload development server
- [ ] Multi-format input support (HTML, MDX, etc.)
- [ ] Theme system
- [ ] Deployment integrations (Netlify, Vercel, GitHub Pages)

## 🤝 Contributing

We welcome contributions! Please follow these guidelines:

1. **Fork** the repository
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Make your changes** and ensure:
   - All tests pass (`pytest`)
   - New features include tests
   - Code follows existing style patterns
   - Type annotations are complete
4. **Commit** your changes: `git commit -m 'Add amazing feature'`
5. **Push** to the branch: `git push origin feature/amazing-feature`
6. **Open a Pull Request**

### Development Setup

```bash
# Clone your fork
git clone https://github.com/your-username/ssg-gex.git
cd ssg-gex

# Set up development environment
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]

# Run pre-commit checks
pytest
mypy src/
black --check src/
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆚 Why SSG-GEX?

Unlike complex site generators, SSG-GEX focuses on:

- **🎯 Simplicity**: Easy to understand and extend
- **🔒 Type Safety**: Catch errors before deployment with comprehensive type annotations
- **⚡ Performance**: Fast builds and minimal overhead
- **🔧 Flexibility**: Node-based architecture allows custom extensions
- **🧪 Quality**: Extensive test coverage ensures reliability
- **🐍 Modern**: Built with the latest Python 3.13+ features

Perfect for developers who want a modern, type-safe approach to static site generation without the complexity of traditional systems.

## 📊 Statistics

- **Language**: Python 3.13+
- **Tests**: 115 comprehensive tests
- **Coverage**: 100% test coverage
- **Architecture**: Type-safe node-based design
- **Dependencies**: Minimal (pytest only)
- **License**: MIT

## 🔗 Links

- [Documentation](https://github.com/your-username/ssg-gex/wiki)
- [Issue Tracker](https://github.com/your-username/ssg-gex/issues)
- [Discussions](https://github.com/your-username/ssg-gex/discussions)
- [PyPI Package](https://pypi.org/project/ssg-gex/)

---

<div align="center">

**Built with ❤️ using Python 3.13+**

[![Python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://python.org)
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

</div>