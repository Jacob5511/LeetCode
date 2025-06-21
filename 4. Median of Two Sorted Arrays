class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        sp = sorted(nums1 + nums2)
        n = len(sp)
        if n % 2 == 0:
            return (sp[n//2] + sp[n//2 - 1]) / 2
        return sp[n // 2]
