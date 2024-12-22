class Solution:
    def climbStairs(self, n: int) -> int:
        # Time complexity of this solution: O(n)
        # store solution at each value of n computed
        # memo[0] is skipped in stairs_rec because n >= 1
        memo = [-1] * (n + 1)

        # recursively explore all paths from the top down
        def stairs_rec(s: int) -> int:
            # base case 1: bad path
            if s < 0:
                return 0
            # base case 2: good path
            if s == 0:
                return 1
            # base case 3: already calculated possible steps at this value of s
            if memo[s] != -1:
                return memo[s]
            
            # check both 1 or 2 steps from current path and store value in memo
            memo[s] = stairs_rec(s - 2) + stairs_rec(s - 1)

            return memo[s]  # final element of memo is the solution

        return stairs_rec(n)
