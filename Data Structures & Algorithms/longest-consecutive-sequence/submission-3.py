class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = defaultdict(int)
        max_len = 0

        for num in nums:
            if not seen[num]:
                left = seen[num-1]
                right = seen[num+1]

                cur_seq_len = left + right + 1
                seen[num] = cur_seq_len

                seen[num - left] = cur_seq_len
                seen[num + right] = cur_seq_len

                max_len = max(max_len, cur_seq_len)

        return max_len

        
        

