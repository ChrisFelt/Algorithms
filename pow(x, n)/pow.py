class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # edge case: always return 0 if x is 0
        if x == 0:
            return 0

        def divide_and_conquer(x, n):
            # base case: n is 0
            if n == 0:
                return 1

            # since x^n * x^n = x^(n + n)
            # find return value at half n and multiply by itself
            temp = divide_and_conquer(x, n // 2)
            temp = temp * temp

            # if n was odd, multiply one last time b x, otherwise return temp
            return temp * x if n % 2 == 1 else temp

        # compute power as if n were positive
        output = divide_and_conquer(x, abs(n))

        # since x^-n = 1 / x^n
        # when n is negative, return the inverse
        if n < 0:
            output = 1 / output

        # round to the 5th decimal place
        return round(output, 5)
