class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def backTrack(path):
            if len(path) == len(nums):
                res.append(path.copy())
                return
            for num in nums:
                if num not in path:
                    path.append(num)
                    backTrack(path)
                    path.pop()
        
        res = []
        backTrack([])
        return res