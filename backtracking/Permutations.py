# https://leetcode.com/problems/permutations/description/
from typing import List


class Permutations:
    def permuteSolutionOne(self, nums: List[int]) -> List[List[int]]:
        result = []
        if len(nums) == 1:
            return [nums[:]]

        for i in range(1):
            n = nums.pop(0)
            perms = self.permuteSolutionOne(nums)

            for perm in perms:
                perm.append(n)

            result.extend(perms)
            nums.append(n)

        return result

    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []

        def helper(index):
            # base case
            if index == n - 1:
                res.append(nums[:])
                return

            # recursive case
            for j in range(index, n):
                nums[index], nums[j] = nums[j], nums[index]
                helper(index + 1)
                nums[index], nums[j] = nums[j], nums[index]

        helper(0)

        return res

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []

        def helper(i):
            # base case
            if i == n - 1:
                res.append(nums[:])

            # recursive case
            hash = {}
            for j in range(i, len(nums)):
                if nums[j] not in hash:
                    hash[nums[j]] = True
                    nums[i], nums[j] = nums[j], nums[i]
                    helper(i + 1)
                    nums[i], nums[j] = nums[j], nums[i]

        helper(0)
        return res


def test():
    permute = Permutations()

    result = permute.permuteSolutionOne([1,2,3])
    print(result)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test()
