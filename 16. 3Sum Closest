class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        # res = set()
        a, dif = 0, 98324798
        # print(nums)
        for i in range(len(nums)):
            left, right = i + 1, len(nums) - 1
            if left >= right:
                # dif_1 = abs(target - nums[-1] - nums[-2] - nums[-3])
                # if dif_1 < dif:
                #     a = nums[-1] + nums[-2] + nums[-3]
                # if abs(target - (nums[0] + nums[1] + nums[2])) < dif_1:
                #     a = nums[0] + nums[1] + nums[2]
                break
            s = nums[i] + nums[left] + nums[right]
            # res.add(s)
            if abs(target - s) < dif:
                a = s
                dif = abs(target - s)
            # print(i, left, right, 'owjojngfouisfn')

            while left < right:
                s = nums[i] + nums[left] + nums[right]
                # print((i, left, right, dif, a, s))

                if abs(target - s) < dif:
                    a = s
                    dif = abs(target - s)
                if s == target:
                    # res.add((nums[i], nums[left], nums[right]))
                    return target
                if s > target:
                    right -= 1
                else:
                    left += 1
        return a
