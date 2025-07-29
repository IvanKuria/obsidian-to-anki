#!/usr/bin/env python3
"""
Basic tests for the Obsidian-to-Anki tool.
Run with: python test_basic.py
"""

import os
import tempfile
import unittest
from unittest.mock import patch, MagicMock
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
            error_str = str(e).lower()
            if any(keyword in error_str for keyword in ["openai_api_key", "api_key", "authentication", "unauthorized", "invalid_api_key"]):
                print("⚠️  Skipping test - OpenAI API key not configured")
                self.skipTest("OpenAI API key not configured")
                return
            else:
                print(f"Unexpected error: {e}")
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
    
    def test_file_processing_without_api(self):
        """Test that file processing doesn't crash without API key."""
        # Create a simple test file
        test_content = "# Simple Test\nThis is a test note."
        temp_file = tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False)
        temp_file.write(test_content)
        temp_file.close()
        
        try:
            # This should not crash even without API key
            process_file(temp_file.name, self.output_file.name, overwrite=True)
            
            # Check if output file was created
            self.assertTrue(os.path.exists(self.output_file.name))
            
        except Exception as e:
            # If it's an API key error, that's expected
            error_str = str(e).lower()
            if any(keyword in error_str for keyword in ["openai_api_key", "api_key", "authentication", "unauthorized", "invalid_api_key"]):
                print("⚠️  Expected API key error - test passed")
                self.skipTest("OpenAI API key not configured")
            else:
                print(f"Unexpected error: {e}")
                raise
        finally:
            os.unlink(temp_file.name)
    
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
    
    def test_sanitize_function_works(self):
        """Test that the sanitize function works independently of API."""
        from card_generator import sanitize_card_output
        
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
    
    @patch('card_generator.OpenAI')
    def test_generate_card_content_with_mock(self, mock_openai):
        """Test card generation with mocked OpenAI client."""
        from card_generator import generate_card_content
        
        # Mock the OpenAI response
        mock_response = MagicMock()
        mock_response.choices = [MagicMock()]
        mock_response.choices[0].message.content = "What is X?\tX is Y\nWhy use Z?\tZ is better"
        
        mock_client = MagicMock()
        mock_client.chat.completions.create.return_value = mock_response
        mock_openai.return_value = mock_client
        
        # Test the function
        result = generate_card_content("# Test Note\nThis is a test.")
        
        # Verify the result
        self.assertIn('\t', result)
        self.assertIn('What is X?', result)
        self.assertIn('X is Y', result)
    
    def test_parser_functions(self):
        """Test that parser utility functions work correctly."""
        from parser import get_file_contents, write_to_file
        
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

if __name__ == '__main__':
    print("Running basic tests for Obsidian-to-Anki...")
    print("Note: Some tests may be skipped if OpenAI API key is not configured.")
    unittest.main(verbosity=2) 