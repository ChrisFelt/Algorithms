class Solution(object):
    def comboSumRecurse(self, curr, solution, total, candidates, target, output):
        """
        :param curr: int, current index
        :param solution: List[int]
        :param total: int
        :param candidates: List[int]
        :param target: int
        :param output: List[int]
        :rtype: None
        """
        # base case 1: when target reached, add solution set to output
        if total == target:
            output.append([])
            for i in range(len(solution)):
                output[len(output) - 1]. append(solution[i])
            return

        # base case 2: do not add solution set to output if current index exceeds
        # the length of candidates or total exceeds target
        if total > target or curr >= len(candidates):
            return

        # add current index of candidates to solution set, sum total numbers in set, and recurse
        # using the current index
        solution.append(candidates[curr])
        self.comboSumRecurse(curr, solution, total + candidates[curr], candidates, target, output)

        # backtrack by removing last element from the solution set and recursing with the next
        # element of candidates
        solution.pop()
        self.comboSumRecurse(curr + 1, solution, total, candidates, target, output)

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # Time complexity of this solution: O(2^n) since each recursive call calls itself twice
        output = []

        # complete temp_output with backtracking function
        self.comboSumRecurse(0, [], 0, candidates, target, output)

        return output
