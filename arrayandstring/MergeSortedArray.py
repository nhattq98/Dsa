from typing import List


# ref: https://leetcode.com/problems/merge-sorted-array
# approach
# an efficient approach since it ensures the larger elements automatically occupy the last indices.
#
# edge cases
# if m is zero , replace nums1 with nums 2
# if n is zero , nothing to do, return nums1
#
# two-pointer technique
# init two pointer i and j to point the last elements with actual value nums1 and nums2
# pointer k to point the last position of the merged array
#
# iterate and merge


class MergeSortedArray:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if m == 0:
            nums1[:] = nums2[:n]
            return
        if n == 0:
            return

        i, j = m - 1, n - 1
        k = m + n - 1

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
