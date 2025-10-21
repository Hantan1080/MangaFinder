# test_mangafinder.py
"""
Tests for MangaFinder module.
"""

import unittest
from mangafinder import MangaFinder

class TestMangaFinder(unittest.TestCase):
    """Test cases for MangaFinder class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MangaFinder()
        self.assertIsInstance(instance, MangaFinder)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MangaFinder()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
