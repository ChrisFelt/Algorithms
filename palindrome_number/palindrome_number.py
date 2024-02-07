from collections import deque


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Time complexity of this solution: O(n)
        # handle edge cases
        if x < 0:
            return False

        # single digit numbers are a palindrome
        if x < 10:
            return True

        # mod and divide by 10 until each digit in x is separated into a list (O(n) complexity)
        # deque data structure gives O(1) complexity for append/pop on both ends of the stack
        x_deque = deque([])
        while x >= 10:
            x_deque.appendleft(x % 10)
            x = x // 10  # remove last digit
        x_deque.appendleft(x)

        # compare the digits and check if palindrome
        # Time complexity for recursion through the deque: O(n)
        return self.recursePalindrome(x_deque)

    def recursePalindrome(self, deque):
        """
        :type deque: Deque[int]
        :rtype: bool
        """
        cur_len = len(deque)
        # base case 1: 1 or 0 digits remaining
        if cur_len == 1 or cur_len == 0:
            return True

        # base case 2: left and right side do not match
        elif deque.popleft() != deque.pop():
            return False

        else:
            return self.recursePalindrome(deque)
