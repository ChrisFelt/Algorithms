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

    def test_003(self):
        # setup test
        check_solution = Solution()
        root = check_solution.create_tree([1])
        target = 0
        test_solution = check_solution.pathSum(root, target)
        answer = 0

        # compare answer to solution
        self.assertTrue(test_solution == answer)

    def test_004(self):
        # setup test
        check_solution = Solution()
        root = check_solution.create_tree([-2, None, -3])
        target = -3
        test_solution = check_solution.pathSum(root, target)
        answer = 1

        # compare answer to solution
        self.assertTrue(test_solution == answer)

    def test_005(self):
        # setup test
        check_solution = Solution()
        root = check_solution.create_tree([2, None, 3])
        target = 3
        test_solution = check_solution.pathSum(root, target)
        answer = 1

        # compare answer to solution
        self.assertTrue(test_solution == answer)

    def test_006(self):
        # setup test
        check_solution = Solution()
        root = check_solution.create_tree([1, None, 1])
        target = 0
        test_solution = check_solution.pathSum(root, target)
        answer = 0

        # compare answer to solution
        self.assertTrue(test_solution == answer)

    def test_007(self):
        # setup test
        check_solution = Solution()
        root = check_solution.create_tree([1, -2, -3])
        target = -2
        test_solution = check_solution.pathSum(root, target)
        answer = 2

        # compare answer to solution
        self.assertTrue(test_solution == answer)

    def test_008(self):
        # setup test
        check_solution = Solution()
        root = check_solution.create_tree([0, 1, 1])
        target = 1
        test_solution = check_solution.pathSum(root, target)
        answer = 4

        # compare answer to solution
        self.assertTrue(test_solution == answer)

    def test_009(self):
        # setup test
        check_solution = Solution()
        root = check_solution.create_tree([1, -2, -3, 1, 3, -2, None, -1])
        target = -1
        test_solution = check_solution.pathSum(root, target)
        answer = 4

        # compare answer to solution
        self.assertTrue(test_solution == answer)


if __name__ == '__main__':
    unittest.main()
