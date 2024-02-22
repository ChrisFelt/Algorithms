import unittest
from pow import Solution


class TestSolution(unittest.TestCase):

    # test the given solutions
    def test_001(self):
        # setup test
        check_solution = Solution()
        x = 2.00000
        n = 10
        test = check_solution.myPow(x, n)
        answer = 1024.00000

        # find shorthand for the following:
        # 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2

        self.assertTrue(test == answer)

    def test_002(self):
        # setup test
        check_solution = Solution()
        x = 2.10000
        n = 3
        test = check_solution.myPow(x, n)
        answer = 9.26100

        self.assertTrue(test == answer)

    def test_003(self):
        # setup test
        check_solution = Solution()
        x = 2.00000
        n = -2
        test = check_solution.myPow(x, n)
        answer = 0.25000

        self.assertTrue(test == answer)

    def test_004(self):
        # setup test
        check_solution = Solution()
        x = 34.00515
        n = -3
        test = check_solution.myPow(x, n)
        answer = 0.00003

        self.assertTrue(test == answer)


if __name__ == '__main__':
    unittest.main()
