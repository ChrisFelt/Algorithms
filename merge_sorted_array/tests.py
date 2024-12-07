import unittest
from merge import Solution


class TestSolution(unittest.TestCase):

    # test the given solutions
    def test_001(self):
        # setup test
        check_solution = Solution()
        nums1 = [1, 2, 3, 0, 0, 0]
        m = 3
        nums2 = [2, 5, 6]
        n = 3
        output = [1, 2, 2, 3, 5, 6]
        test_solution = check_solution.merge(nums1, m, nums2, n)

        # compare answer to solution
        self.assertTrue(test_solution == output)

    def test_002(self):
        # setup test
        check_solution = Solution()
        nums1 = [1]
        m = 1
        nums2 = []
        n = 0
        output = [1]
        test_solution = check_solution.merge(nums1, m, nums2, n)

        # compare answer to solution
        self.assertTrue(test_solution == output)
    
    def test_003(self):
        # setup test
        check_solution = Solution()
        nums1 = [0]
        m = 0
        nums2 = [1]
        n = 1
        output = [1]
        test_solution = check_solution.merge(nums1, m, nums2, n)

        # compare answer to solution
        self.assertTrue(test_solution == output)


if __name__ == '__main__':
    unittest.main()
