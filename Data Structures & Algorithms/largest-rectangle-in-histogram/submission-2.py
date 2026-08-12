class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = [] # (index, height)
        n = len(heights)
        max_area = 0

        for i in range(n):
            idx = i
            while stack and heights[i] < stack[-1][1]:
                idx, h = stack.pop()
                max_area = max(max_area, (i-idx) * h)
            else:
                stack.append((idx, heights[i]))
        
        for i, h in stack:
            max_area = max(max_area, (n-i)*h)

        return max_area
