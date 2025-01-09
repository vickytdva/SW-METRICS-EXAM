"""
This module contains test cases for the math.pow function.
It tests the function with various cases, including edge cases, to ensure correctness.
"""

import math

class TestMathPow:
    """
    This class contains test cases for the math.pow function.
    It covers tests for normal cases, negative exponents, and edge cases.
    """

    def test_positive_exponent(self):
        """
        Test case for a positive exponent.
        """
        assert math.pow(2, 3) == 8

    def test_zero_exponent(self):
        """
        Test case for zero exponent.
        """
        assert math.pow(2, 0) == 1

    def test_negative_exponent(self):
        """
        Test case for a negative exponent.
        """
        assert math.pow(2, -2) == 0.25

    def test_negative_base_even_exponent(self):
        """
        Test case for a negative base with an even exponent.
        """
        assert math.pow(-2, 2) == 4

    def test_negative_base_odd_exponent(self):
        """
        Test case for a negative base with an odd exponent.
        """
        assert math.pow(-2, 3) == -8

    def test_edge_case_zero_base(self):
        """
        Test case for base zero with a positive exponent.
        """
        assert math.pow(0, 3) == 0

    def test_edge_case_negative_zero_base(self):
        """
        Test case for base zero with a negative exponent.
        """
        assert math.pow(0, -1) == float('inf')  # Should raise infinity

