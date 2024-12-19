import unittest
from sqrt import Solution


class TestSolution(unittest.TestCase):

    # test the given solutions
    def test_001(self):
        # setup test
        check_solution = Solution()
        x = 4
        output = 2
        test_solution = check_solution.mySqrt(x)

        # compare answer to solution
        self.assertTrue(test_solution == output)

    def test_002(self):
        # setup test
        check_solution = Solution()
        x = 8
        output = 2
        test_solution = check_solution.mySqrt(x)

        # compare answer to solution
        self.assertTrue(test_solution == output)
    
    # other tests
    def test_003(self):
        # setup test
        check_solution = Solution()
        x = 3
        output = 1
        test_solution = check_solution.mySqrt(x)

        # compare answer to solution
        self.assertTrue(test_solution == output)
    
    def test_004(self):
        # setup test
        check_solution = Solution()
        x = 0
        output = 0
        test_solution = check_solution.mySqrt(x)

        # compare answer to solution
        self.assertTrue(test_solution == output)
    
    def test_005(self):
        # setup test
        check_solution = Solution()
        x = 9
        output = 3
        test_solution = check_solution.mySqrt(x)

        # compare answer to solution
        self.assertTrue(test_solution == output)


if __name__ == '__main__':
    unittest.main()
