# Examples

This directory contains sample markdown files that you can use to test the Obsidian-to-Anki tool.

## Sample Files

- `sample_note.md` - A comprehensive note about the Binary Search algorithm

## Testing the Tool

1. **Test with a single file**:
   ```bash
   python main.py --note examples/sample_note.md --output test_output.txt
   ```

2. **Test with the entire examples directory**:
   ```bash
   python main.py --dir examples --output test_output.txt
   ```

3. **Check the output**:
   ```bash
   cat test_output.txt
   ```

## Expected Output

The tool should generate flashcards like:
```
What is the time complexity of binary search?	O(log n)
Why must the array be sorted for binary search to work?	Because binary search relies on the sorted property to eliminate half of the remaining elements in each iteration.
What is the space complexity of binary search?	O(1) - it only uses a constant amount of extra space.
```

## Adding Your Own Examples

Feel free to add your own markdown files to this directory to test different types of content. The tool works best with:

- Technical documentation
- Study notes
- Programming concepts
- Algorithm explanations
- Language learning notes

## Tips for Good Flashcards

- Write clear, focused notes
- Include code examples when relevant
- Use headings and structure to organize information
- Include both concepts and practical examples 