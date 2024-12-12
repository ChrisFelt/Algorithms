import unittest
from add_binary import Solution


class TestSolution(unittest.TestCase):

    # test the given solutions
    def test_001(self):
        # setup test
        check_solution = Solution()
        a = "11"
        b = "1"
        output = "100"
        test_solution = check_solution.addBinary(a, b)

        # compare answer to solution
        self.assertTrue(test_solution == output)

    def test_002(self):
        # setup test
        check_solution = Solution()
        a = "1010"
        b = "1011"
        output = "10101"
        test_solution = check_solution.addBinary(a, b)

        # compare answer to solution
        self.assertTrue(test_solution == output)
    
    # additional tests
    def test_003(self):
        # setup test
        check_solution = Solution()
        a = "0"
        b = "0"
        output = "0"
        test_solution = check_solution.addBinary(a, b)

        # compare answer to solution
        self.assertTrue(test_solution == output)

if __name__ == '__main__':
    unittest.main()
