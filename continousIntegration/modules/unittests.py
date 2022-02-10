import unittest
import sys
import os
sys.path.append('./')
from test import test
from compilation import compile
from notification import notify


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
        Test 7: Tests if it returns ERROR if no valid authentication token is given
        
        See Also
        --------
        modules.test : Tests 1-3 tests the test function
        modules.compilation :  Tests 4-6 tests the compile function
    """
    
    # Test 1
    def test_empty(self):
        status , code = test('./tests/test1')
        self.assertTrue(code == 0)

    # Test 2
    def test_successful(self):
        status , code = test('./tests/test2')
        self.assertTrue(code == 0)

    # Test 3
    def test_fails(self):
        status , code = test('./tests/test3')
        self.assertFalse(code == 0)

    # Test 4
    def test_empty_com(self):
        status , code = compile('./tests/test4')
        self.assertTrue(code == 0)
    
    # Test 5   
    def test_successful_com(self):
        status , code = compile('./tests/test5')
        self.assertTrue(code == 0)
    
    # Test 6
    def test_fails_com(self):
        status , code = compile('./tests/test6')
        self.assertFalse(code == 0)

    # Test 7 
    def test_fails_notify(self):
        data = {
            "after": "f04a518bc7c57bff8fad020262f9fc16c7ac35f3", 
            "repository": {
                "full_name": "soderqw/DD2480_Lab2-CI",
            }
        }
        status , code = notify(data, "success", 0)
        self.assertTrue(code != 0)


         
if __name__ == '__main__':
    unittest.main()