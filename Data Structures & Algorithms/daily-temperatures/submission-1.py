class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for curr_day in range(len(temperatures)):
            curr_temp = temperatures[curr_day]
            
            while stack and curr_temp > temperatures[stack[-1]]:
                popped_index = stack.pop()
                res[popped_index] = curr_day - popped_index
                
            stack.append(curr_day)
            
        return res