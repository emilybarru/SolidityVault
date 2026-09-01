# test_solidityvault.py
"""
Tests for SolidityVault module.
"""

import unittest
from solidityvault import SolidityVault

class TestSolidityVault(unittest.TestCase):
    """Test cases for SolidityVault class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SolidityVault()
        self.assertIsInstance(instance, SolidityVault)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SolidityVault()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
