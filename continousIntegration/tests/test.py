import unittest
import sys
import os
sys.path.append('../')
from modules.test import test 
from modules.compilation import compile 


class Tests(unittest.TestCase):
    """ Tests the test function.
        Tests
        -----
        Test 1: Tests if it returns SUCCESS when there are no tests to run.
        Test 2: Tests if it returns SUCCESS when all tests pass.
        Test 3: Tests if it returns ERROR if at least one test fails.
        Test 4: Tests if it returns SUCCESS if there are not tests in the directory
        Test 5: Tests if it returns SUCCESS when all the tests in the directory can compile
        Test 6: Tests if it returns ERROR if at least one of the files in the directory cannot compile
        
        See Also
        --------
        modules.test : Tests 1-3 tests the test function
        modules.compilation :  Tests 4-6 tests the compile function
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
        self.assertFalse(status == 'ERROR')
    
    # Test 4
    def test_empty_com(self):
        status , _ = compile('./test4/tests')
        self.assertTrue(status == 'SUCCESS')
    
    # Test 5   
    def test_successful_com(self):
        status , _ = compile('./test5/tests')
        self.assertTrue(status == 'SUCCESS')
    
    # Test 6
    def test_fails_com(self):
        status , _ = compile('./test6/tests')
        self.assertFalse(status == 'ERROR')
         
if __name__ == '__main__':
    unittest.main()