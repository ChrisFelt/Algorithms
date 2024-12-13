import unittest
from title_to_no import Solution


class TestSolution(unittest.TestCase):

    # test the given solutions
    def test_001(self):
        # setup test
        check_solution = Solution()
        input = "A"
        output = 1
        test_solution = check_solution.merge(input)

        # compare answer to solution
        self.assertTrue(test_solution == output)

    def test_002(self):
# setup test
        check_solution = Solution()
        input = "AB"
        output = 28
        test_solution = check_solution.merge(input)

        # compare answer to solution
        self.assertTrue(test_solution == output)
    
    def test_003(self):
        # setup test
        check_solution = Solution()
        input = "ZY"
        output = 701
        test_solution = check_solution.merge(input)

        # compare answer to solution
        self.assertTrue(test_solution == output)


if __name__ == '__main__':
    unittest.main()
