class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        h_set = set(nums)
        longest = 0
        for num in nums:
            if (num-1) not in h_set:
                seq_length = 1
                while (num + seq_length) in h_set:
                    seq_length += 1
                longest = max(seq_length, longest)
        return longest