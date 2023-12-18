from unittests_for_calculator import CalculatorUnittest
import unittest

class Unittest_calculator_runner:

    def run_unittest (self):

        # Load unit tests from CalculatorTest
        test_suite = unittest.TestLoader().loadTestsFromTestCase(CalculatorUnittest)

        # Create a test runner with output to a file
        with open('test_results.txt', 'w') as f:
            runner = unittest.TextTestRunner(stream=f, verbosity=2)
            runner.run(test_suite)

