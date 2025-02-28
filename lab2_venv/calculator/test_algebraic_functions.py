"""
Unit tests for the calculator library
"""
import os, sys

# Add project root to Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.insert(0, project_root)

from .src.utils import add, subtract, multiply, divide

class TestCalculator:
    # Testing the add
    def test_effective_addition(self):
        assert 4 == add(2, 2), "The addition is not correct"

    
    def test_addition_failure(self):
        assert 5 != add('a', 3), "The input must be a number"

    # Testing the subtract
    def test_effective_subtraction(self):
        assert 2 == subtract(4, 2)
    

    def test_subtraction_failure(self):
        assert 2 != subtract('a', 3), "The input must be a number"
    
    # Testing the multiply
    def test_effective_multiplication(self):
        assert 8 == multiply(4, 2)


    def test_multiplication_failure(self):
        assert 8 != multiply('a', 3), "The input must be a number"
    
    # Testing the divide
    def test_effective_division(self):
        assert 2 == divide(4, 2)


    def test_division_failure(self):
        assert 2 != divide('a', 3), "The input must be a number"
    