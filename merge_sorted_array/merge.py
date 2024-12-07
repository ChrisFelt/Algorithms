class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # time complexity of this solution is O(k + n). High memory usage, but faster than solutions using sort.
        # copy nums1 to new list: nums1_copy (O(n))
        nums1_copy = nums1.copy()

        # set separate counters for nums1_copy and nums2 to 0
        nums1_ind = 0
        nums2_ind = 0

        # counter for nums1 current element
        i = 0
        # iterate through nums1 until we reach m
        # time complexity for this loop: O(k + n)
        while nums1_ind < m:
            # merge current index of nums2 into nums1 if it is less than the current index of nums1
            if nums2_ind < n and nums1_copy[nums1_ind] >= nums2[nums2_ind]:
                nums1[i] = nums2[nums2_ind]
                nums2_ind += 1

            # otherwise merge current index of nums1_copy into nums1
            else:
                nums1[i] = nums1_copy[nums1_ind]
                nums1_ind += 1
            
            i += 1
        
        # merge any remaining elements of nums2
        while nums2_ind < n:
                nums1[i] = nums2[nums2_ind]
                nums2_ind += 1
                i += 1

        return nums1