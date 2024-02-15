import unittest
from combo_sum import Solution


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
        nums = [2, 3, 6, 7]
        target = 7
        solution = [[2, 2, 3], [7]]
        check_solution = Solution()

        # get test results and sort
        test = check_solution.combinationSum(nums, target)
        sort_all(test)
        sort_all(solution)

        # check against solution
        self.assertTrue(compare_lists(test, solution))

    def test002(self):
        # setup test
        nums = [2, 3, 5]
        target = 8
        solution = [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
        check_solution = Solution()

        # get test results and sort
        test = check_solution.combinationSum(nums, target)
        sort_all(test)
        sort_all(solution)

        # check against solution
        self.assertTrue(compare_lists(test, solution))

    def test003(self):
        # setup test
        nums = [2]
        target = 1
        solution = []
        check_solution = Solution()

        # get test results and sort
        test = check_solution.combinationSum(nums, target)
        sort_all(test)
        sort_all(solution)

        # check against solution
        self.assertTrue(compare_lists(test, solution))

    # edge case: lots of candidates!
    def test004(self):
        # setup test
        nums = [2, 3, 4, 5, 6, 7, 8, 9, 10]
        target = 12
        solution = [[2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 4], [2, 2, 2, 3, 3], [2, 2, 2, 6], [2, 2, 3, 5], [2, 2, 4, 4],
                    [2, 2, 8], [2, 3, 3, 4], [2, 3, 7], [2, 4, 6], [2, 5, 5], [2, 10], [3, 3, 3, 3], [3, 3, 6],
                    [3, 4, 5], [3, 9], [4, 4, 4], [4, 8], [5, 7], [6, 6]]

        check_solution = Solution()

        # get test results and sort
        test = check_solution.combinationSum(nums, target)
        sort_all(test)
        sort_all(solution)

        # check against solution
        self.assertTrue(compare_lists(test, solution))

    def test005(self):
        # setup test
        nums = []
        target = 1
        solution = []
        check_solution = Solution()

        # get test results and sort
        test = check_solution.combinationSum(nums, target)
        sort_all(test)
        sort_all(solution)

        # check against solution
        self.assertTrue(compare_lists(test, solution))


if __name__ == '__main__':
    unittest.main()
