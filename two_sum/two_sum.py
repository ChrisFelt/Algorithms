class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Time complexity for this solution: O(n)
        # store numbers in a dictionary for quick access
        store_nums = {}

        cur_index = 0

        # iterate through nums
        # Time complexity: O(n)
        for i in nums:

            # current number needed to reach target
            cur_num = target - i

            # check if target reached
            # Time complexity of accessing dictionary with key: O(1)
            if cur_num in store_nums:
                return [store_nums[cur_num], cur_index]

            # otherwise add current index of nums to the dictionary
            else:
                store_nums[i] = cur_index
                cur_index += 1

        # no combination of numbers adds to the target
        return None
