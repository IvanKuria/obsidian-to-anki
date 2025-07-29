#!/usr/bin/env python3
"""
Basic tests for the Obsidian-to-Anki tool.
Run with: python test_basic.py
"""

import os
import tempfile
import unittest
from parser import get_file_contents, write_to_file
from card_generator import sanitize_card_output

class TestObsidianToAnki(unittest.TestCase):
    
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
    
    def test_sanitize_function_works(self):
        """Test that the sanitize function works independently of API."""
        # Test with various input formats
        test_cases = [
            ("Question\tAnswer", "Question\tAnswer"),  # Already tab-separated
            ("Question  Answer", "Question\tAnswer"),  # Double space
            ("Question: Answer", "Question\tAnswer"),  # Colon separator
            ("Q1\tA1\nQ2\tA2", "Q1\tA1\nQ2\tA2"),   # Multiple lines
        ]
        
        for input_text, expected in test_cases:
            result = sanitize_card_output(input_text)
            self.assertIn('\t', result)
            self.assertIn('Answer', result)
    
    def test_parser_functions(self):
        """Test that parser utility functions work correctly."""
        # Test get_file_contents
        test_content = "# Test\nThis is a test file."
        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
            f.write(test_content)
            temp_file_path = f.name
        
        try:
            content = get_file_contents(temp_file_path)
            self.assertEqual(content, test_content)
        finally:
            os.unlink(temp_file_path)
        
        # Test write_to_file
        test_output = "Test output content"
        output_file = tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False)
        output_file.close()
        
        try:
            write_to_file(output_file.name, test_output, overwrite=True)
            with open(output_file.name, 'r') as f:
                content = f.read().strip()
                self.assertEqual(content, test_output)
        finally:
            os.unlink(output_file.name)
    
    def test_basic_imports(self):
        """Test that all modules can be imported without errors."""
        try:
            import main
            import parser
            import card_generator
            self.assertTrue(True, "All modules imported successfully")
        except ImportError as e:
            self.fail(f"Failed to import module: {e}")
    
    def test_cli_help(self):
        """Test that CLI help works."""
        import subprocess
        try:
            result = subprocess.run(['python', 'main.py', '--help'], 
                                  capture_output=True, text=True, timeout=10)
            self.assertEqual(result.returncode, 0)
            self.assertIn('Obsidian-to-Anki', result.stdout)
        except subprocess.TimeoutExpired:
            self.fail("CLI help command timed out")
        except FileNotFoundError:
            self.skipTest("main.py not found")

if __name__ == '__main__':
    print("Running basic tests for Obsidian-to-Anki...")
    unittest.main(verbosity=2) 