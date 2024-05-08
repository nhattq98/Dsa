from typing import List


# ref: https://leetcode.com/problems/remove-duplicates-from-sorted-array
# topic: two-pointer, array
class RemoveDuplicates:
    def removeDuplicates(self, nums: List[int]) -> int:
        encounter = nums[0]
        index = 1

        for i in range(1, len(nums)):
            if encounter != nums[i]:
                nums[index] = nums[i]
                encounter = nums[i]
                index += 1

        return index

