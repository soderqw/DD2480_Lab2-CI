import unittest
import os
import sys

sys.path.append('continousIntegration/')
from modules import compilation
from modules import test as testModule

class modulesTest(unittest.TestCase):
    '''
        Runs unit tests on each of the local components of two kinds, one that succeeds and one that fails.
        Some of the tests are dynamically created in order to force the correct error codes to be expected.
        
        Tests
        -----
        test_ClonePath: Tests if the cloned directory exists.
        test_Compile_True: Tests if the correct code is returned from compile module for a file that is supposed to compile.
        test_Compile_False: Tests if the correct code is returned from compile module for a file that is not supposed to compile.
        test_Test_True: Tests if the correct code is returned from testing module during a scenario where no test fails (empty folder).
        test_Test_False: Tests if the correct code is returned from testing module during a scenario where a test fails.

        See Also
        --------
        compilation.py : Functions the compile all python files within a given file path.
        test.py : Functions that runs the unit tests of the repository.
    ''' 
    def test_ClonePath(self):
        self.assertTrue(os.path.isdir('../DD2480_LAB2-CI'))

    def test_Compile_True(self):
        # Run the compilation within an empty folder (should succeed).
        os.mkdir('testCompile')
        _, code = compilation.compile(os.getcwd() + '/testCompile')
        os.rmdir(os.getcwd() + '/testCompile') # Cleans up the created directory.

        self.assertTrue(code == 0)
        self.assertFalse(code != 0)

    def test_Compile_False(self):
        # Run the compilation within a folder containing an erronous file (should fail).
        os.mkdir('testCompile')

        with open(os.getcwd() + '/testCompile/fail.py', 'w') as f:
            f.write('print(')

        _, code = compilation.compile(os.getcwd() + '/testCompile')

        os.remove(os.getcwd() + '/testCompile/fail.py')
        os.rmdir(os.getcwd() + '/testCompile') # Cleans up the created directory.

        self.assertTrue(code != 0)
        self.assertFalse(code == 0)

    def test_Test_True(self):
        #Run the compilation within an empty folder (should succeed).
        os.mkdir('testTest')
        _, code = testModule.test(os.getcwd() + '/testTest')
        print(os.getcwd() + '/testTest')
        os.rmdir(os.getcwd() + '/testTest') # Cleans up the created directory.

        self.assertTrue(code == 0)
        self.assertFalse(code != 0)

    def test_Test_False(self):
        #Run the compilation within an empty folder (should succeed).
        with open(os.getcwd() + '/tests/fail.py', 'w') as f:
            f.write('import unittest; assertTrue(False)')
            #f.write('import sys; sys.exit(1)') # Simulates an execution error on one line.

        _, code = testModule.test(os.getcwd())

        os.remove(os.getcwd() + '/tests/fail.py')

        self.assertTrue(code != 0)
        self.assertFalse(code == 0)
        

if __name__ == '__main__':
    unittest.main()