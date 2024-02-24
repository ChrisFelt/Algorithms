import unittest
from path_sum_III import Solution


class TestSolution(unittest.TestCase):

    # test the given solutions
    def test_001(self):
        # setup test
        check_solution = Solution()
        root = check_solution.create_tree([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1])
        target = 8
        test_solution = check_solution.pathSum(root, target)
        answer = 3

        # compare answer to solution
        self.assertTrue(test_solution == answer)

    def test_002(self):
        # setup test
        check_solution = Solution()
        root = check_solution.create_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1])
        target = 22
        test_solution = check_solution.pathSum(root, target)
        answer = 3

        # compare answer to solution
        self.assertTrue(test_solution == answer)


if __name__ == '__main__':
    unittest.main()
