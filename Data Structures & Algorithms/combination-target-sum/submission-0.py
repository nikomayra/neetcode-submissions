class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backTrack(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return

            if i >= len(nums) or total > target:
                return

            cur.append(nums[i])
            backTrack(i, cur, total + nums[i])
            cur.pop()
            backTrack(i + 1, cur, total)

        backTrack(0, [], 0)
        return res

