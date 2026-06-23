class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        def backTrack(start, path, cur):
            if cur == target:
                res.append(path.copy())
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                if cur + candidates[i] > target:
                    break

                path.append(candidates[i])
                backTrack(i + 1, path, cur + candidates[i])
                path.pop()

        res = []
        candidates.sort()
        backTrack(0, [], 0)
        return res