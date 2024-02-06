import unittest
from two_sum import Solution


class TestCheckPwd(unittest.TestCase):

    # test the given solutions
    def test_001(self):
        # setup test
        nums = [2, 7, 11, 15]
        target = 9
        check_solution = Solution()

        solution = [0, 1]

        # call two_sum method from Solution and check if correct
        self.assertTrue(check_solution.twoSum(nums, target) == solution)

    def test_002(self):
        # setup test
        nums = [3, 2, 4]
        target = 6
        check_solution = Solution()

        solution = [1, 2]

        # call two_sum method from Solution and check if correct
        self.assertTrue(check_solution.twoSum(nums, target) == solution)

    def test_003(self):
        # setup test
        nums = [3, 3]
        target = 6
        check_solution = Solution()

        solution = [0, 1]

        # call two_sum method from Solution and check if correct
        self.assertTrue(check_solution.twoSum(nums, target) == solution)

    # test no solution edge case
    def test_004(self):
        # setup test
        nums = [3, 3, 3, 3, 3, 3, 3]
        target = 7
        check_solution = Solution()

        # call two_sum method from Solution and check if correct
        self.assertIsNone(check_solution.twoSum(nums, target))

    # test negative numbers
    def test_005(self):
        # setup test
        nums = [-8, -2, 1, -9, -7, -3, -5]
        target = -13
        check_solution = Solution()

        solution = [0, 6]

        # call two_sum method from Solution and check if correct
        self.assertTrue(check_solution.twoSum(nums, target) == solution)


if __name__ == '__main__':
    unittest.main()
