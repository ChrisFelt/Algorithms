import unittest
from title_to_no import Solution


class TestSolution(unittest.TestCase):

    # test the given solutions
    def test_001(self):
        # setup test
        check_solution = Solution()
        input = "A"
        output = 1
        test_solution = check_solution.titleToNumber(input)

        # compare answer to solution
        self.assertTrue(test_solution == output)

    def test_002(self):
        # setup test
        check_solution = Solution()
        input = "AB"
        output = 28
        test_solution = check_solution.titleToNumber(input)

        # compare answer to solution
        self.assertTrue(test_solution == output)
    
    def test_003(self):
        # setup test
        check_solution = Solution()
        input = "ZY"
        output = 701
        test_solution = check_solution.titleToNumber(input)

        # compare answer to solution
        self.assertTrue(test_solution == output)
    
    # additional tests
    def test_004(self):
        # setup test
        check_solution = Solution()
        input = "AAA"
        output = 703
        test_solution = check_solution.titleToNumber(input)

        # compare answer to solution
        self.assertTrue(test_solution == output)
    
    def test_004(self):
        # setup test
        check_solution = Solution()
        input = "AAAAAAA"
        output = 321272407
        test_solution = check_solution.titleToNumber(input)

        # compare answer to solution
        self.assertTrue(test_solution == output)


if __name__ == '__main__':
    unittest.main()
