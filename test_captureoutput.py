# test_captureoutput.py
"""
Tests for CaptureOutput module.
"""

import unittest
from captureoutput import CaptureOutput

class TestCaptureOutput(unittest.TestCase):
    """Test cases for CaptureOutput class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CaptureOutput()
        self.assertIsInstance(instance, CaptureOutput)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CaptureOutput()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
