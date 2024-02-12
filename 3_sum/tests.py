import unittest
from three_sum import Solution


def sort_all(lst):
    """
    :param lst: List[List[int]]
    :return: List[Set(int)]
    """
    # sort all nested lists then lst
    for i in lst:
        i.sort()

    lst.sort()


def compare_lists(lst1, lst2):
    """
    :param lst1: List[List(int)]
    :param lst2: List[List(int)]
    :return: bool
    """
    # return False if lists vary in length
    if len(lst1) != len(lst2):
        return False

    # return False if lst1 contains a set that is not in lst2
    for i in lst1:
        if i not in lst2:
            return False

    return True  # all sets in lst1 are in lst2 and vice versa


class TestSolution(unittest.TestCase):

    # test the given solutions
    def test_001(self):
        # setup test
        nums = [-1, 0, 1, 2, -1, -4]
        solution = [[-1, -1, 2], [-1, 0, 1]]
        check_solution = Solution()

        # get test results and sort
        test = check_solution.threeSum(nums)
        sort_all(test)
        sort_all(solution)

        # check against solution
        self.assertTrue(compare_lists(test, solution))

    def test_002(self):
        # setup test
        nums = [0, 1, 1]
        solution = []
        check_solution = Solution()

        # get test results and sort
        test = check_solution.threeSum(nums)
        sort_all(test)
        sort_all(solution)

        # check against solution
        self.assertTrue(compare_lists(test, solution))

    def test_003(self):
        # setup test
        nums = [0, 0, 0]
        solution = [[0, 0, 0]]
        check_solution = Solution()

        # get test results and sort
        test = check_solution.threeSum(nums)
        sort_all(test)
        sort_all(solution)

        # check against solution
        self.assertTrue(compare_lists(test, solution))

    def test_004(self):
        # setup test
        nums = [-3, -3, -1, -1, 0, 0, 0, 1, 1, 2, 3]
        solution = [[-3, 3, 0], [-3, 2, 1], [-1, -1, 2], [-1, 0, 1], [0, 0, 0]]
        check_solution = Solution()

        # get test results and sort
        test = check_solution.threeSum(nums)
        sort_all(test)
        sort_all(solution)

        # check against solution
        self.assertTrue(compare_lists(test, solution))

    def test_005(self):
        # setup test
        nums = []
        solution = []
        check_solution = Solution()

        # get test results and sort
        test = check_solution.threeSum(nums)
        sort_all(test)
        sort_all(solution)

        # check against solution
        self.assertTrue(compare_lists(test, solution))


if __name__ == '__main__':
    unittest.main()
