class Solution:
    def twoSum(self, nums, target):
        seen = {}

        for i, num in enumerate(nums):
            rem = target - num
            if rem in seen:
                return [seen[rem], i]
            seen[num] = i
