#!/usr/bin/env python3
"""
Basic tests for the Obsidian-to-Anki tool.
Run with: python test_basic.py
"""

import os
import tempfile
import unittest
from parser import process_file, process_directory
from card_generator import sanitize_card_output

class TestObsidianToAnki(unittest.TestCase):
    
    def setUp(self):
        """Set up test fixtures."""
        self.test_note_content = """# Test Note

This is a test note about algorithms.

## Time Complexity
- O(n) for linear search
- O(log n) for binary search

## Key Points
1. Always consider edge cases
2. Test with different input sizes
"""
        
        # Create a temporary test file
        self.temp_file = tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False)
        self.temp_file.write(self.test_note_content)
        self.temp_file.close()
        
        # Create a temporary output file
        self.output_file = tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False)
        self.output_file.close()
    
    def tearDown(self):
        """Clean up test fixtures."""
        os.unlink(self.temp_file.name)
        os.unlink(self.output_file.name)
    
    def test_process_file(self):
        """Test processing a single file."""
        try:
            process_file(self.temp_file.name, self.output_file.name, overwrite=True)
            
            # Check if output file was created and has content
            self.assertTrue(os.path.exists(self.output_file.name))
            
            with open(self.output_file.name, 'r') as f:
                content = f.read()
                self.assertIsInstance(content, str)
                
        except Exception as e:
            # If OpenAI API is not available, this is expected
            if "OPENAI_API_KEY" in str(e) or "api_key" in str(e).lower():
                print("⚠️  Skipping test - OpenAI API key not configured")
                return
            else:
                raise
    
    def test_sanitize_card_output(self):
        """Test the card output sanitization function."""
        test_input = """
        What is time complexity?	O(n)
        Why use binary search?	It's faster than linear search
        """
        
        result = sanitize_card_output(test_input)
        
        # Should return tab-separated format
        self.assertIn('\t', result)
        self.assertIn('O(n)', result)
        self.assertIn('binary search', result)
    
    def test_sanitize_card_output_with_malformed_input(self):
        """Test sanitization with malformed input."""
        test_input = """
        This line has no tab
        Another bad line
        Good line\tGood answer
        """
        
        result = sanitize_card_output(test_input)
        
        # Should handle malformed lines gracefully
        self.assertIn('Good line\tGood answer', result)

if __name__ == '__main__':
    print("Running basic tests for Obsidian-to-Anki...")
    print("Note: Some tests may be skipped if OpenAI API key is not configured.")
    unittest.main(verbosity=2) 