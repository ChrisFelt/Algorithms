import unittest
from combo_sum_II import Solution


def sort_all(lst):
    """
    :param lst: List[List[int]]
    :return: None, sorts in place
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
        nums = [10, 1, 2, 7, 6, 1, 5]
        target = 8
        solution = [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
        check_solution = Solution()

        # get test results and sort
        test = check_solution.combinationSum2(nums, target)
        sort_all(test)
        sort_all(solution)

        # check against solution
        self.assertTrue(compare_lists(test, solution))

    def test_002(self):
        # setup test
        nums = [2, 5, 2, 1, 2]
        target = 5
        solution = [[1, 2, 2], [5]]
        check_solution = Solution()

        # get test results and sort
        test = check_solution.combinationSum2(nums, target)
        sort_all(test)
        sort_all(solution)

        # check against solution
        self.assertTrue(compare_lists(test, solution))

    def test_003(self):
        # setup test
        nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        target = 27
        solution = []
        check_solution = Solution()

        # get test results and sort
        test = check_solution.combinationSum2(nums, target)
        sort_all(test)
        sort_all(solution)
        # check against solution
        self.assertTrue(compare_lists(test, solution))

    def test_004(self):
        # setup test
        nums = [2, 2, 2]
        target = 4
        solution = [[2, 2]]
        check_solution = Solution()

        # get test results and sort
        test = check_solution.combinationSum2(nums, target)
        sort_all(test)
        sort_all(solution)
        # check against solution
        self.assertTrue(compare_lists(test, solution))


if __name__ == '__main__':
    unittest.main()
