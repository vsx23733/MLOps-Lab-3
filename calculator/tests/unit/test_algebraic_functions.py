import os, sys

# Add project root to Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.insert(0, project_root)

from src.utils import add, subtract, multiply, divide


class TestCalculator:

    def test_addition(self):
        assert 4 == add(2, 2)

    def test_subtraction(self):
        assert 2 == subtract(4, 2)

    def test_multiplication(self):
        assert 6 == multiply(2, 3)

    def test_division(self):
        assert 2 == divide(4, 2)

    def test_division_by_zero(self):
        try:
            divide(4, 0)
            assert False, "Expected ZeroDivisionError"
        except ZeroDivisionError:
            assert True
