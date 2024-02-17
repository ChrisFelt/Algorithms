import unittest
from pascals_triangle import Solution


class TestSolution(unittest.TestCase):

    # test the given solutions
    def test_001(self):
        # setup test
        rows = 5
        answer = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
        check_solution = Solution()
        solution = check_solution.generate(rows)

        # compare answer to solution
        self.assertTrue(solution == answer)

    def test_002(self):
        # setup test
        rows = 1
        answer = [[1]]
        check_solution = Solution()
        solution = check_solution.generate(rows)

        # compare answer to solution
        self.assertTrue(solution == answer)

    # test a big number of rows
    def test_003(self):
        # setup test
        rows = 10
        answer = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1],
                  [1, 6, 15, 20, 15, 6, 1], [1, 7, 21, 35, 35, 21, 7, 1], [1, 8, 28, 56, 70, 56, 28, 8, 1],
                  [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]]
        check_solution = Solution()
        solution = check_solution.generate(rows)

        # compare answer to solution
        self.assertTrue(solution == answer)


if __name__ == '__main__':
    unittest.main()
