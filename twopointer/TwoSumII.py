from typing import List


class TwoSumII:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        size = len(numbers)
        i = 0
        j = size - 1
        while i < j:
            if numbers[i] + numbers[j] == target:
                return [i + 1, j + 1]
            elif numbers[i] + numbers[j] > target:
                j = j - 1
            else:
                i = i + 1

        return []

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        size = len(nums)
        result = []
        nums.sort()

        for i in range(size):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j = i + 1
            k = size - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total > 0:
                    k -= 1
                elif total < 0:
                    i += 1
                else:
                    result.append([nums[i], nums[j], nums[k]])

        return result
