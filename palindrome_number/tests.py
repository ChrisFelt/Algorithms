import unittest
from palindrome_number import Solution


class TestCheckPwd(unittest.TestCase):

    # test the given solutions
    def test_001(self):
        # setup test
        x = 121
        check_solution = Solution()

        # call isPalindrome method from Solution to test
        self.assertTrue(check_solution.isPalindrome(x) is True)

    def test_002(self):
        # setup test
        x = -121
        check_solution = Solution()

        # call isPalindrome method from Solution to test
        self.assertTrue(check_solution.isPalindrome(x) is False)

    def test_003(self):
        # setup test
        x = 10
        check_solution = Solution()

        # call isPalindrome method from Solution to test
        self.assertTrue(check_solution.isPalindrome(x) is False)

    # additional test cases
    def test_004(self):
        # setup test
        x = 0
        check_solution = Solution()

        # call isPalindrome method from Solution to test
        self.assertTrue(check_solution.isPalindrome(x) is True)

    # large number of digits, same value
    def test_005(self):
        # setup test
        x = 1111111111111
        check_solution = Solution()

        # call isPalindrome method from Solution to test
        self.assertTrue(check_solution.isPalindrome(x) is True)

    # large, odd number of digits, different values
    def test_006(self):
        # setup test
        x = 232323232323
        check_solution = Solution()

        # call isPalindrome method from Solution to test
        self.assertTrue(check_solution.isPalindrome(x) is False)

    # large, even number of digits, different values
    def test_007(self):
        # setup test
        x = 23233232
        check_solution = Solution()

        # call isPalindrome method from Solution to test
        self.assertTrue(check_solution.isPalindrome(x) is True)


if __name__ == '__main__':
    unittest.main()
