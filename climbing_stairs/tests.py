import unittest
from climb_stairs import Solution


class TestSolution(unittest.TestCase):

    # test the given solutions
    def test_001(self):
        # setup test
        check_solution = Solution()
        n = 2
        output = 2
        test_solution = check_solution.climbStairs(n)

        # compare answer to solution
        self.assertTrue(test_solution == output)

    def test_002(self):
        # setup test
        check_solution = Solution()
        n = 3
        output = 3
        test_solution = check_solution.climbStairs(n)

        # compare answer to solution
        self.assertTrue(test_solution == output)

    def test_003(self):
        # setup test
        check_solution = Solution()
        n = 10
        output = 89
        test_solution = check_solution.climbStairs(n)

        # compare answer to solution
        self.assertTrue(test_solution == output)


if __name__ == '__main__':
    unittest.main()
