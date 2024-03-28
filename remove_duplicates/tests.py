import unittest
from remove_duplicates import Solution


class TestSolution(unittest.TestCase):

    # test the given solutions
    def test_001(self):
        # setup test
        nums = [1, 1, 2]
        k = 2
        check_solution = Solution()

        solution = [1, 2]

        # check that k is found correctly
        self.assertTrue(check_solution.removeDuplicates(nums) == k)

        # check that duplicates removed from array
        self.assertTrue(nums[:k] == solution)

    def test_002(self):
        # setup test
        nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        k = 5
        check_solution = Solution()

        solution = [0, 1, 2, 3, 4]

        # check that k is found correctly
        self.assertTrue(check_solution.removeDuplicates(nums) == k)

        # check that duplicates removed from array
        self.assertTrue(nums[:k] == solution)


if __name__ == '__main__':
    unittest.main()
