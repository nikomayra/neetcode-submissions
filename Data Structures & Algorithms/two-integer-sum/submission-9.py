class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}

        for i in range(len(nums)):
            num = nums[i]
            delta = target - num
            if delta in seen:
                return [seen[delta], i]
            seen[num] = i