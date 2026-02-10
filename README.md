# SSG-GEX: Modern Python Static Site Generator

A clean, type-safe static site generator built with modern Python 3.13. SSG-GEX transforms your content into fast, secure websites using a node-based architecture that provides both simplicity and extensibility.

## Features

- **Type-Safe Architecture**: Built with comprehensive type annotations for reliability and IDE support
- **Node-Based Design**: Extensible HTML node system supporting complex content structures
- **Rich Text Support**: Native support for plain text, bold, italic, code, links, and images
- **Markdown Processing**: Complete markdown to HTML conversion with block-level and inline formatting
- **Comprehensive Testing**: Full test coverage with pytest ensuring code quality
- **Modern Python**: Uses Python 3.13+ features for clean, maintainable code

## Core Components

### Text Processing
- **TextNode**: Handles various text types (plain, bold, italic, code, links, images)
- **TextType Enum**: Type-safe text classification system
- **Text-to-HTML Pipeline**: Converts markdown with inline formatting to semantic HTML

### HTML Generation
- **HTMLNode**: Core HTML element with support for tags, values, children, and properties
- **LeafNode**: Specialized leaf nodes for terminal elements
- **ParentNode**: Container nodes with multiple children
- **Smart Rendering**: Automatic HTML generation with proper attribute handling

### Markdown Processing
- **Block Detection**: Identifies paragraphs, headings, code blocks, quotes, and lists
- **Inline Parsing**: Handles bold (**text**), italic (_text_), code (`text`), links, and images
- **Structure Preservation**: Maintains document hierarchy with proper nesting

## Installation

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

## Quick Start

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

## Architecture

SSG-GEX follows a clean, modular architecture:

1. **Text Nodes**: Handle semantic content classification
2. **HTML Nodes**: Convert text into structured HTML
3. **Content Pipeline**: Transform markdown/text into static sites
4. **Block Processing**: Parse markdown blocks into appropriate HTML elements

## Development

```bash
# Run tests
pytest

# Run tests with coverage
pytest --cov=src

# Run specific test file
pytest src/nodes/htmlnode_test.py -v

# Run markdown processing tests
pytest src/utils/markdown_to_html_nodes_test.py -v
```

## Supported Markdown Features

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

## Testing Philosophy

SSG-Gex emphasizes comprehensive testing with:
- Unit tests for all core components
- Type checking throughout the codebase
- Edge case validation
- Performance testing for large content
- Markdown parsing accuracy tests

## Current Status ✅

### Completed Features
- [x] Complete markdown to HTML conversion
- [x] All block-level elements support
- [x] All inline formatting support
- [x] Type-safe node architecture
- [x] Comprehensive test coverage

## Roadmap

- [ ] Template system integration
- [ ] Plugin architecture
- [ ] CLI interface
- [ ] Asset processing (CSS/JS optimization)
- [ ] Multi-format input support (HTML, MD, etc.)
- [ ] Development server with live reload
- [ ] Deployment integrations

## Contributing

Contributions are welcome! Please ensure:
- All tests pass (`pytest`)
- New features include tests
- Code follows existing style patterns
- Type annotations are complete

## License

MIT License - see LICENSE file for details.

## Why SSG-GEX?

Unlike complex site generators, SSG-GEX focuses on:
- **Simplicity**: Easy to understand and extend
- **Type Safety**: Catch errors before deployment
- **Performance**: Fast builds and minimal overhead
- **Flexibility**: Node-based architecture allows custom extensions

Perfect for developers who want a modern, type-safe approach to static site generation without the complexity of traditional systems.