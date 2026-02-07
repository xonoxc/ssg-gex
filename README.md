# SSG-GEX: Modern Python Static Site Generator

A clean, type-safe static site generator built with modern Python 3.13. SSG-GEX transforms your content into fast, secure websites using a node-based architecture that provides both simplicity and extensibility.

## Features

- **Type-Safe Architecture**: Built with comprehensive type annotations for reliability and IDE support
- **Node-Based Design**: Extensible HTML node system supporting complex content structures
- **Rich Text Support**: Native support for plain text, bold, italic, code, links, and images
- **Comprehensive Testing**: Full test coverage with pytest ensuring code quality
- **Modern Python**: Uses Python 3.13+ features for clean, maintainable code

## Core Components

### Text Processing
- **TextNode**: Handles various text types (plain, bold, italic, code, links, images)
- **TextType Enum**: Type-safe text classification system

### HTML Generation
- **HTMLNode**: Core HTML element with support for tags, values, children, and properties
- **LeafNode**: Specialized leaf nodes for terminal elements
- **Smart Rendering**: Automatic HTML generation with proper attribute handling

## Installation

```bash
# Clone the repository
git clone https://github.com/your-username/ssg-gex.git
cd ssg-gex

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -e .
```

## Quick Start

```python
from src.nodes.textnode import TextNode, TextType

# Create different types of text content
plain_text = TextNode("Hello World", TextType.PLAIN)
bold_text = TextNode("Important", TextType.BOLD_TEXT)
link_text = TextNode("Click me", TextType.LINK_TEXT, "https://example.com")

# Convert to HTML (coming soon)
# html_content = generate_html([plain_text, bold_text, link_text])
```

## Architecture

SSG-GEX follows a clean, modular architecture:

1. **Text Nodes**: Handle semantic content classification
2. **HTML Nodes**: Convert text into structured HTML
3. **Content Pipeline**: Transform markdown/text into static sites (in development)

## Development

```bash
# Run tests
pytest

# Run tests with coverage
pytest --cov=src

# Run specific test file
pytest src/nodes/htmlnode_test.py -v
```

## Testing Philosophy

SSG-Gex emphasizes comprehensive testing with:
- Unit tests for all core components
- Type checking throughout the codebase
- Edge case validation
- Performance testing for large content

## Roadmap

- [ ] Markdown parsing support
- [ ] Template system integration
- [ ] Plugin architecture
- [ ] CLI interface
- [ ] Asset processing (CSS/JS optimization)
- [] Multi-format input support (HTML, MD, etc.)
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