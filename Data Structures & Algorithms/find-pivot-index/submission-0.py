class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # recompute prefix sum array:
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        for i, num in enumerate(nums):
            prefix_sum[i + 1] = prefix_sum[i] + num
            
        # find leftmost pivot
        for i in range(n):
            left_sum = prefix_sum[i]
            right_sum = prefix_sum[-1] - prefix_sum[i + 1]
            if left_sum == right_sum:
                return i
        return -1
