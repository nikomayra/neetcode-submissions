class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(0, len(nums)):
            for j in range(0, len(nums)):
                if i == j:
                    continue
                if nums[i] == nums[j]:
                    return True
        return False