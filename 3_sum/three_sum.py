class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Time Complexity of this solution: O(n^2)
        output = []
        nums.sort()

        # iterate through all possible combinations of elements in nums (O(n))
        i = 0
        while i < len(nums) - 1:
            # if current element > 0 there can be no 3sum that = 0
            if nums[i] <= 0:
                # skip all repeated numbers in the first position
                if i - 1 >= 0:
                    if nums[i] == nums[i - 1]:
                        i += 1
                        continue

                # traverse remaining numbers with high and low pointers (O(n))
                low = i + 1
                high = len(nums) - 1
                while low < high:

                    # skip all repeated numbers in the third position for the current first position
                    if high + 1 < len(nums):
                        if nums[high] == nums[high + 1]:
                            high -= 1
                            continue
                    # find number that would make 3sum = 0
                    target_num = nums[i] + nums[low] + nums[high]
                    if target_num == 0:
                        output.append([nums[i], nums[low], nums[high]])
                        high -= 1
                        low += 1

                    elif target_num > 0:  # move high pointer when sum > 0
                        high -= 1

                    else:  # move low pointer when sum < 0
                        low += 1

                i += 1

            else:
                break  # no numbers remaining <= 0

        return output


class FirstTry(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # No initial list sorting in this solution, with resulting extremely high memory cost
        # Overall complexity: O(n^2) average O(n^3) worst case
        nums_dict = {}
        output = []
        nums_len = len(nums)

        # initialize memo with all elements of nums as keys for average O(1) access (O(n) worst case)
        for i in nums:
            if i in nums_dict:
                nums_dict[i]["count"] += 1
            else:
                nums_dict[i] = {}  # nested dictionary!!!
                nums_dict[i]["count"] = 1

        # iterate through all possible combinations of elements in nums (O(n))
        for i in range(nums_len):
            j = i + 1
            # iterate through remaining numbers (O(n))
            while j < nums_len:
                # find number that would make 3sum = 0
                target_num = -1 * (nums[i] + nums[j])

                # if target_num in nums and this 3sum combo is not already memoized,
                # add to output and memoize entry (this step is O(n) worst case)
                if target_num in nums_dict:
                    if nums[i] in nums_dict[target_num] and nums[j] in nums_dict[target_num]:
                        j += 1
                        continue

                    if target_num == nums[i] and nums_dict[target_num]["count"] == 1:
                        j += 1
                        continue
                    elif target_num == nums[j] and nums_dict[target_num]["count"] == 1:
                        j += 1
                        continue
                    elif target_num == nums[i] == nums[j] == 0 and nums_dict[target_num]["count"] < 3:
                        j += 1
                        continue

                    output.append([target_num, nums[i], nums[j]])
                    # memoize all possible combinations
                    nums_dict[target_num][nums[j]] = None
                    nums_dict[target_num][nums[i]] = None
                    nums_dict[nums[j]][target_num] = None
                    nums_dict[nums[j]][nums[i]] = None
                    nums_dict[nums[i]][target_num] = None
                    nums_dict[nums[i]][nums[j]] = None
                j += 1

        return output
