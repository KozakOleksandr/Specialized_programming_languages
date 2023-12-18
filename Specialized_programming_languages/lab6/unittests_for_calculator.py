import unittest
from unittest.mock import patch
from lab2.calculator_engine import Calculator_engine


class CalculatorUnittest(unittest.TestCase):

    def setUp(self):
        # Initialization of the calculator object before each test
        self.calculator = Calculator_engine()

    # Test cases for addition
    def test_positive_numbers_addition(self):
        result = self.calculator.calculateValue(3, 7, '+')
        self.assertEqual(result, 10, "Addition of positive numbers is incorrect")

    def test_negative_numbers_addition(self):
        result = self.calculator.calculateValue(-5, -3, '+')
        self.assertEqual(result, -8, "Addition of negative numbers is incorrect")

    def test_mixed_numbers_addition(self):
        result = self.calculator.calculateValue(8, -4, '+')
        self.assertEqual(result, 4, "Addition of mixed numbers is incorrect")

    def test_zero_addition(self):
        result = self.calculator.calculateValue(0, 12, '+')
        self.assertEqual(result, 12, "Addition with zero is incorrect")

    # Test cases for subtraction
    def test_positive_numbers_subtraction(self):
        result = self.calculator.calculateValue(10, 4, '-')
        self.assertEqual(result, 6, "Subtraction of positive numbers is incorrect")

    def test_negative_numbers_subtraction(self):
        result = self.calculator.calculateValue(-5, -3, '-')
        self.assertEqual(result, -2, "Subtraction of negative numbers is incorrect")

    def test_mixed_numbers_subtraction(self):
        result = self.calculator.calculateValue(8, -4, '-')
        self.assertEqual(result, 12, "Subtraction of mixed numbers is incorrect")

    def test_zero_subtraction(self):
        result = self.calculator.calculateValue(0, 7, '-')
        self.assertEqual(result, -7, "Subtraction with zero is incorrect")

    # Test cases for multiplication
    def test_positive_numbers_multiplication(self):
        result = self.calculator.calculateValue(5, 3, '*')
        self.assertEqual(result, 15, "Multiplication of positive numbers is incorrect")

    def test_negative_numbers_multiplication(self):
        result = self.calculator.calculateValue(-4, -2, '*')
        self.assertEqual(result, 8, "Multiplication of negative numbers is incorrect")

    def test_mixed_numbers_multiplication(self):
        result = self.calculator.calculateValue(6, -2, '*')
        self.assertEqual(result, -12, "Multiplication of mixed numbers is incorrect")

    def test_zero_multiplication(self):
        result = self.calculator.calculateValue(8, 0, '*')
        self.assertEqual(result, 0, "Multiplication with zero is incorrect")

    # Test cases for division
    def test_positive_numbers_division(self):
        result = self.calculator.calculateValue(10, 2, '/')
        self.assertEqual(result, 5, "Division of positive numbers is incorrect")

    def test_negative_numbers_division(self):
        result = self.calculator.calculateValue(-6, -2, '/')
        self.assertEqual(result, 3, "Division of negative numbers is incorrect")

    def test_mixed_numbers_division(self):
        result = self.calculator.calculateValue(8, -2, '/')
        self.assertEqual(result, -4, "Division of mixed numbers is incorrect")

    def test_zero_division(self):
        result = self.calculator.calculateValue(0, 7, '/')
        self.assertEqual(result, 0, "Division involving zero should return 0")

    # Test cases for getOperator method
    @patch('builtins.input', side_effect=['/', '√'])
    def test_getOperator_valid_operators(self, mock_input):
        # The calls to getOperator should succeed with valid operators ('/', '√')
        for expected_result in ('/', '√'):
            result = self.calculator.getOperator("Enter an operator: ")
            self.assertEqual(result, expected_result)

    @patch('builtins.input', side_effect=['+', '-', 'invalid', '*', '^'])
    def test_getOperator_invalid_then_valid_operators(self, mock_input):
        # The first call to getOperator should fail with an invalid operator ('invalid')
        with self.assertRaises(ValueError):
            self.calculator.getOperator("Enter an operator: ")

        # The next calls to getOperator should succeed with valid operators ('+', '*', '^')
        for expected_result in ('+', '*', '^'):
            result = self.calculator.getOperator("Enter an operator: ")
            self.assertEqual(result, expected_result)

    # Test case for getParamValue method
    @patch('builtins.input', side_effect=['abc', 5])
    def test_getParamValue_invalid_input_then_valid_input(self, mock_input):
        result = self.calculator.getParamValue("Enter a number: ")
        self.assertEqual(result, 5.0)
