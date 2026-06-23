class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_speed = dict(zip(position, speed))
        stack = []
        for p in sorted(position)[::-1]:
            stack.append((target - p)/car_speed[p])
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)