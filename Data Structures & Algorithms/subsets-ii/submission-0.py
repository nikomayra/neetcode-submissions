class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        def backTrack(start):
            res.append(subset.copy())
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                subset.append(nums[i])
                backTrack(i + 1)
                subset.pop()

        res = []
        subset = []
        nums.sort()
        backTrack(0)
        return res