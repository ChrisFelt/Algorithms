import unittest
from path_sum_II import Solution


class TestSolution(unittest.TestCase):

    # test the given solutions
    def test_001(self):
        # setup test
        check_solution = Solution()
        root = check_solution.create_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1])
        target = 22
        test_solution = check_solution.has_path_sum_II(root, target)
        answer = [[5, 4, 11, 2], [5, 8, 4, 5]]

        # compare answer to solution
        self.assertTrue(test_solution == answer)

    def test_002(self):
        # setup test
        check_solution = Solution()
        root = check_solution.create_tree([1, 2, 3])
        target = 5
        test_solution = check_solution.has_path_sum_II(root, target)
        answer = []

        # compare answer to solution
        self.assertTrue(test_solution == answer)

    # check empty
    def test_003(self):
        # setup test
        check_solution = Solution()
        root = check_solution.create_tree([])
        target = 5
        test_solution = check_solution.has_path_sum_II(root, target)
        answer = []

        # compare answer to solution
        self.assertTrue(test_solution == answer)

    # test negative values
    def test004(self):
        # setup test
        check_solution = Solution()
        root = check_solution.create_tree([-5, -4, -8, -11, None, -13, -4, -7, -2, None, None, -5, -1])
        target = -22
        test_solution = check_solution.has_path_sum_II(root, target)
        answer = [[-5, -4, -11, -2], [-5, -8, -4, -5]]

        # compare answer to solution
        self.assertTrue(test_solution == answer)


if __name__ == '__main__':
    unittest.main()
