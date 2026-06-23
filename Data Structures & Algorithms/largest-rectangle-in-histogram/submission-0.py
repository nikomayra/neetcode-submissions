class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        maybe_left_limits = [] # indeces
        heights = heights + [0] # force right limit

        for i, bar in enumerate(heights):
            while maybe_left_limits and heights[maybe_left_limits[-1]] > bar:
                height = heights[maybe_left_limits.pop()]
                if not maybe_left_limits:
                    width = i
                else:
                    width = i - maybe_left_limits[-1] - 1
                max_area = max(max_area, height*width)
            maybe_left_limits.append(i)
        return max_area


            
            