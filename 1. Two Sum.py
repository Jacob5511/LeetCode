class Solution:
    def twoSum(self, nums: list, target: int):
        s = set(nums)
        for i in range(len(nums)):
            a = nums[i]
            t = target - a
            if t in s:
                for j in range(i+1,len(nums)):
                    if nums[j] == t:
                        return [i, j]
