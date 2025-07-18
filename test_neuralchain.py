# test_neuralchain.py
"""
Tests for NeuralChain module.
"""

import unittest
from neuralchain import NeuralChain

class TestNeuralChain(unittest.TestCase):
    """Test cases for NeuralChain class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NeuralChain()
        self.assertIsInstance(instance, NeuralChain)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NeuralChain()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
