# Contributing to Obsidian-to-Anki

Thank you for your interest in contributing to Obsidian-to-Anki! This document provides guidelines and information for contributors.

## How Can I Contribute?

### Reporting Bugs
- Use the GitHub issue tracker
- Include a clear description of the bug
- Provide steps to reproduce the issue
- Include your operating system and Python version
- If possible, include a sample markdown file that reproduces the issue

### Suggesting Enhancements
- Use the GitHub issue tracker with the "enhancement" label
- Describe the feature and why it would be useful
- Include any mockups or examples if applicable

### Code Contributions
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Add tests if applicable
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## Development Setup

1. **Fork and clone the repository**:
   ```bash
   git clone https://github.com/yourusername/obsidian-to-anki.git
   cd obsidian-to-anki
   ```

2. **Set up a virtual environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your environment**:
   Create a `.env` file with your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

## Code Style

- Follow PEP 8 style guidelines
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions focused and single-purpose
- Add comments for complex logic

## Testing

Before submitting a pull request, please:

1. Test your changes with sample markdown files
2. Ensure the output format is correct (tab-separated)
3. Test both single file and directory processing
4. Verify error handling works as expected

## Project Structure

```
obsidian-to-anki/
├── main.py              # CLI interface
├── parser.py            # File processing logic
├── card_generator.py    # AI-powered flashcard generation
├── requirements.txt     # Python dependencies
├── README.md           # Project documentation
├── CONTRIBUTING.md     # This file
├── LICENSE             # MIT License
└── examples/           # Sample files for testing
```

## Pull Request Guidelines

- Provide a clear description of the changes
- Include any relevant issue numbers
- Add tests if applicable
- Update documentation if needed
- Ensure all tests pass

## Questions?

If you have questions about contributing, feel free to:
- Open an issue on GitHub
- Ask in the discussions section
- Contact the maintainers directly

Thank you for contributing to Obsidian-to-Anki! 🎉 