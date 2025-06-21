class Solution:
    def maxArea(self, height: list) -> int:
        m = 0
        left = 0
        right = len(height) - 1
        while left < right:
            m_height = min(height[left], height[right])
            m = max(m_height * (right - left), m)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return m
