class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # Time complexity of this solution: O(2^n)
        candidates.sort()
        output = []
        temp_solution = []

        # recursive backtracking
        def recurse(cur, total):
            # base case 1: total == target
            if total == target:
                output.append(temp_solution[:])  # splice contents of solution and append to output

            # base case 2: total > target
            if total > target:
                return

            for k in range(cur, len(candidates)):
                # prevent duplicate solutions by skipping duplicates in the sorted candidates
                if k > cur and candidates[k - 1] == candidates[k]:
                    continue

                # add to solution set and recurse with next index
                temp_solution.append(candidates[k])
                recurse(k + 1, total + candidates[k])

                # backtrack by popping the last index of the solution
                temp_solution.pop()

        recurse(0, 0)

        return output
