class Solution:
    def climbStairs(self, n: int) -> int:
        # Time complexity of this solution: appears to be O(n!) ...

        # recursively explore all paths
        def stairs_rec(s: int) -> int:
            # base case 1: bad path
            if s < 0:
                return 0
            # base case 2: good path
            if s == 0:
                return 1
            
            # check both 1 or 2 steps from current path
            return stairs_rec(s - 2) + stairs_rec(s - 1)

        return stairs_rec(n)
