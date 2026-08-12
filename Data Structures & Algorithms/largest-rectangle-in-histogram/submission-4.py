class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        left_limits = [] # indices
        n = len(heights)

        for i in range(n + 1):
            while left_limits and (i == n or heights[left_limits[-1]] >= heights[i]):
                h = heights[left_limits.pop()]
                w = i - left_limits[-1] - 1 if left_limits else i
                max_area = max(max_area, h*w)
            left_limits.append(i)
        return max_area