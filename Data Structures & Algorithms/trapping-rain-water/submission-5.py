class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        total_water = 0
        
        for i, h in enumerate(height):
            while stack and h >= height[stack[-1]]:
                mid = stack.pop()
                if stack:
                    left_height = height[stack[-1]]
                    water_height = min(left_height, h) - height[mid]
                    water_width = i - stack[-1] - 1
                    total_water += max(0, water_height * water_width)
            stack.append(i)
        
        return total_water