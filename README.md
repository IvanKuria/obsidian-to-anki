# Obsidian-to-Anki Flashcard Generator

Convert your Obsidian markdown notes into Anki flashcards using AI! This tool automatically extracts key concepts from your notes and generates high-quality flashcards that are perfect for spaced repetition learning.

## Features

- 🧠 **AI-Powered**: Uses GPT-4 to intelligently extract key concepts from your notes
- 📝 **Markdown Support**: Works with any Obsidian markdown files
- 🎯 **Smart Card Generation**: Creates conceptual questions rather than simple definitions
- 📁 **Batch Processing**: Process entire directories or individual files
- 🎨 **Anki-Compatible**: Outputs in the standard Anki import format

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/obsidian-to-anki.git
   cd obsidian-to-anki
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your OpenAI API key**:
   Create a `.env` file in the project root:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

## Usage

### Process a single note
```bash
python main.py --note path/to/your/note.md --output flashcards.txt
```

### Process an entire directory
```bash
python main.py --dir path/to/your/notes/folder --output flashcards.txt
```

### Options
- `--note`: Path to a single markdown file
- `--dir`: Path to a directory containing markdown files
- `--output`: Output file path (default: `anki.txt`)
- `--overwrite`: Overwrite the output file instead of appending

## Example

Given a markdown note about algorithms:
```markdown
# Binary Search

Binary search is an efficient algorithm for finding an element in a sorted array.
Time complexity: O(log n)
Space complexity: O(1)

## Implementation
```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```
```

The tool generates flashcards like:
```
What is the time complexity of binary search?	O(log n)
Why is binary search only applicable to sorted arrays?	Because it relies on the sorted property to eliminate half of the remaining elements in each iteration.
What is the space complexity of binary search?	O(1) - it only uses a constant amount of extra space.
```

## Importing to Anki

1. Run the tool to generate your flashcards
2. Open Anki
3. Go to File → Import
4. Select your generated `.txt` file
5. Choose your deck and note type
6. Import!

## Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Development Setup

1. Fork the repository
2. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```
3. Install development dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with OpenAI's GPT-4 API
- Inspired by the need for better study tools for programmers
- Thanks to the Anki community for the spaced repetition system

## Support

If you encounter any issues or have questions, please [open an issue](https://github.com/yourusername/obsidian-to-anki/issues) on GitHub. 