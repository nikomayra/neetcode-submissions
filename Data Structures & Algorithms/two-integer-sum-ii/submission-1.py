class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while l < r:
            while r > l and numbers[r] > (target - numbers[l]):
                r -= 1
            while l < r and numbers[l] < (target - numbers[r]):
                l += 1
            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]
