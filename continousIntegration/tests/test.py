import unittest
import sys
import os
sys.path.append('../')
from modules.test import test 


class Tests(unittest.TestCase):
    """ Tests the test function.
        Tests
        -----
        Test 1: Tests if it returns SUCCESS when there are no tests to run.
        Test 2: Tests if it returns SUCCESS when all tests pass.
        Test 3: Tests if it returns ERROR if at least one test fails.
        See Also
        --------
        modules.test : Function to test.
        """

    # Test 1
    def test_empty(self):
        status , _ = test('./test1')
        self.assertTrue(status == 'SUCCESS')

    # Test 2
    def test_successful(self):
        status , _ = test('./test2')
        self.assertTrue(status == 'SUCCESS')

    # Test 3
    def test_fails(self):
        status , _ = test('./test3')
        self.assertTrue(status == 'ERROR')
    

if __name__ == '__main__':
    unittest.main()