import unittest
from path_sum import Solution


class TestSolution(unittest.TestCase):

    # test the given solutions
    def test_001(self):
        # setup test
        check_solution = Solution()
        root = check_solution.create_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1])
        target = 22
        solution = check_solution.hasPathSum(root, target)

        # compare answer to solution
        self.assertTrue(solution)

    def test_002(self):
        # setup test
        check_solution = Solution()
        root = check_solution.create_tree([1, 2, 3])
        target = 5
        solution = check_solution.hasPathSum(root, target)

        # compare answer to solution
        self.assertFalse(solution)

    def test_003(self):
        # setup test
        check_solution = Solution()
        root = check_solution.create_tree([])
        target = 0
        solution = check_solution.hasPathSum(root, target)

        # compare answer to solution
        self.assertFalse(solution)

    # test negative values
    def test_004(self):
        # setup test
        check_solution = Solution()
        root = check_solution.create_tree([-2, None, -3])
        target = -5
        solution = check_solution.hasPathSum(root, target)

        # compare answer to solution
        self.assertTrue(solution)


if __name__ == '__main__':
    unittest.main()
