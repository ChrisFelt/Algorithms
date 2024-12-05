import unittest
from plus_one import Solution


class TestSolution(unittest.TestCase):

    # test the given solutions
    def test_001(self):
        # setup test
        check_solution = Solution()
        input = [1, 2, 3]
        output = [1, 2, 4]
        test_solution = check_solution.plusOne(input)

        # compare answer to solution
        self.assertTrue(test_solution == output)

    def test_002(self):
        # setup test
        check_solution = Solution()
        input = [4, 3, 2, 1]
        output = [4, 3, 2, 2]
        test_solution = check_solution.plusOne(input)

        # compare answer to solution
        self.assertTrue(test_solution == output)
    
    def test_003(self):
        # setup test
        check_solution = Solution()
        input = [9]
        output = [1, 0]
        test_solution = check_solution.plusOne(input)

        # compare answer to solution
        self.assertTrue(test_solution == output)


if __name__ == '__main__':
    unittest.main()
