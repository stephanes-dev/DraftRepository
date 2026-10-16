# test_draftrepository.py
"""
Tests for DraftRepository module.
"""

import unittest
from draftrepository import DraftRepository

class TestDraftRepository(unittest.TestCase):
    """Test cases for DraftRepository class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DraftRepository()
        self.assertIsInstance(instance, DraftRepository)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DraftRepository()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
