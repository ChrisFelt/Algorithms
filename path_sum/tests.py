import unittest
from path_sum import Solution


class TestSolution(unittest.TestCase):

    # test the given solutions
    def test_001(self):
        # setup test
        tree = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]
        target = 22
        check_solution = Solution()
        solution = check_solution.has_path_sum(tree, target)

        # compare answer to solution
        self.assertTrue(solution)

    def test_002(self):
        # setup test
        tree = [1, 2, 3]
        target = 5
        check_solution = Solution()
        solution = check_solution.has_path_sum(tree, target)

        # compare answer to solution
        self.assertFalse(solution)

    def test_003(self):
        # setup test
        tree = []
        target = 0
        check_solution = Solution()
        solution = check_solution.has_path_sum(tree, target)

        # compare answer to solution
        self.assertFalse(solution)


if __name__ == '__main__':
    unittest.main()
