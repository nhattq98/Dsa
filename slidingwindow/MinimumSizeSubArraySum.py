from typing import List

class MinimumSizeSubArraySum:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        right = 0
        total = 0
        result = float("inf")
        num_lens = len(nums)

        for left in range(num_lens):
            if left == 0:
                total = nums[left]
            else:
                total = total - nums[left - 1]

            while total < target:
                right += 1
                if right >= num_lens:
                    break
                else:
                    total += nums[right]

            tmp_result = right - left + 1
            result = min(result, tmp_result)
        return result

def test():
    minSubArrayLen = MinimumSizeSubArraySum()
    result = minSubArrayLen.minSubArrayLen(target=11, nums=[1,2,3,4,5])
    print(result)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test()
