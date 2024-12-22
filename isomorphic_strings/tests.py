import unittest
from isomorphic_strings import Solution


class TestSolution(unittest.TestCase):

    # test the given solutions
    def test_001(self):
        # setup test
        check_solution = Solution()
        s = "egg"
        t = "add"
        output = True
        test_solution = check_solution.isIsomorphic(s, t)

        # compare answer to solution
        self.assertTrue(test_solution == output)

    def test_002(self):
        # setup test
        check_solution = Solution()
        s = "foo"
        t = "bar"
        output = False
        test_solution = check_solution.isIsomorphic(s, t)

        # compare answer to solution
        self.assertTrue(test_solution == output)

    def test_003(self):
        # setup test
        check_solution = Solution()
        s = "paper"
        t = "title"
        output = True
        test_solution = check_solution.isIsomorphic(s, t)

        # compare answer to solution
        self.assertTrue(test_solution == output)


if __name__ == '__main__':
    unittest.main()
