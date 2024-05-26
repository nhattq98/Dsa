from typing import List


class MinimumSizeSubArraySum:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        total = 0
        result = -1
        numsLen = len(nums)

        for left in range(len(nums)):
            total = nums[left]
            while total > target:
                right += 1
                if right >= numsLen:
                    return 0

                total += nums[right]

            tmpResult = right - left + 1
            result = min(result, tmpResult)
