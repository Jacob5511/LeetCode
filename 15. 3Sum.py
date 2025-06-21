class Solution:
    def threeSum(self, nums: list[int]):
        nums.sort()
        res = set()
        for i in range(len(nums)):
            left, right = i + 1, len(nums) - 1
            if nums[i] > 0 or left >= right:
                break
            s = nums[i] + nums[left] + nums[right]
            while left < right:
                if s == 0 and (nums[i], nums[left], nums[right]) not in res:
                    res.add((nums[i], nums[left], nums[right]))
                if s > 0:
                    right -= 1
                else:
                    left += 1
                s = nums[i] + nums[left] + nums[right]
        return list(res)
