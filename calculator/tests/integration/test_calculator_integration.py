import os, sys
from unittest.mock import patch
import pytest

# Add project root to Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.insert(0, project_root)

from src.utils import add, subtract, multiply, divide  # Fixed import path

class TestCalculatorIntegration:
    
    def test_full_addition_workflow(self):
        # Test multiple additions in sequence
        assert add(5, 3) == 8
        assert add(-1, 1) == 0
        assert add(0.1, 0.2) == pytest.approx(0.3)  # Handle floating point

    def test_full_subtraction_workflow(self):
        assert subtract(10, 5) == 5
        assert subtract(-1, -1) == 0
        assert subtract(3.5, 2.1) == pytest.approx(1.4)

    def test_full_multiplication_workflow(self):
        assert multiply(4, 3) == 12
        assert multiply(-2, 3) == -6
        assert multiply(2.5, 2) == 5.0

    def test_full_division_workflow(self):
        assert divide(8, 2) == 4
        assert divide(5, 2) == 2.5
        with pytest.raises(ZeroDivisionError):
            divide(5, 0)

    @patch('builtins.input')
    def test_calculator_user_interaction(self, mock_input):
        # Simulate user input sequence: 
        # 1 (add), 5, 3, no (stop)
        mock_input.side_effect = ['1', '5', '3', 'no']
        
        # Import here to avoid global input mocking
        from src.calculator import main
        
        # The main function should run without errors
        try:
            main()
        except SystemExit:
            pass
