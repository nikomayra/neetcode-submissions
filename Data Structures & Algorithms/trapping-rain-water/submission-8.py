class Solution:
    def trap(self, height: List[int]) -> int:
        
        n = len(height)
        max_left_walls = [0]*n
        max_right_walls = [0]*n

        cur_max = 0
        for i in range(n):
            max_left_walls[i] = cur_max
            cur_max = max(cur_max, height[i])

        #print("max_left_walls:",max_left_walls)

        cur_max = 0
        for i in range(n-1, -1, -1):
            max_right_walls[i] = cur_max
            cur_max = max(cur_max, height[i])

        #print("max_right_walls:",max_right_walls)

        total_water = 0
        for i, h in enumerate(height):
            water_i = min(max_left_walls[i], max_right_walls[i]) - h
            water_i = 0 if water_i < 0 else water_i
            # print(water_i)
            total_water += water_i
        
        return total_water
