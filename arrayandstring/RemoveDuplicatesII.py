from typing import List


# ref: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
# topic: two pointer, array
# [1,1,1,2,2,3] -> [1,1,2,2,3,_]
class RemoveDuplicatesII:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 1
        occurrence = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                occurrence += 1
            else:
                occurrence = 1

            if occurrence <= 2:
                nums[index] = nums[i]
                index += 1

        return index
