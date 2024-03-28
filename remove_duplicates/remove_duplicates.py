class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Time complexity of this solution: O(n)
        # empty list edge case
        if len(nums) == 0:
            return 0

        # unique number count
        k = 1

        # last unique integer copied
        last = nums[0]
        # track the current index of nums to check
        cur = 1

        # iterate through nums, target is current index to replace
        for target in range(1, len(nums)):

            # increment cur until it is higher than the last unique integer
            while cur < len(nums) and last == nums[cur]:
                cur += 1

            # copy cur into target
            if cur < len(nums):
                last = nums[cur]  # new unique integer copied
                nums[target] = nums[cur]
                k += 1
            else:
                break  # no more elements to check

        return k


