class Solution:
    def mySqrt(self, x: int) -> int:
        """Using Newton's method"""
        approx = x

        # iterative approximations
        while approx * approx > x:
            # Newton's method applied to finding square roots: x(n+ 1) = 1/2 * (n + a/n), where a is the radicand
            approx = (approx + x // approx) // 2  
        
        return approx