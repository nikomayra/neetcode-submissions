class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # ... thought elements had to be 'in-order' in original array...
        
        # seen = defaultdict(int) # num : con_seq
        # max_con_seq = 1

        # for num in nums:
        #     if num not in seen:
        #         seen[num] += 1
        #     if num-1 in seen:
        #         seen[num] = seen[num-1] + 1
        #         max_con_seq = max(max_con_seq, seen[num])
        # return max_con_seq


        seen = {}
        max_len = 0

        for num in nums:
            if num not in seen:
                left = seen.get(num - 1, 0)
                right = seen.get(num + 1, 0)

                current_len = left + right + 1
                max_len = max(max_len, current_len)

                seen[num] = current_len

                seen[num - left] = current_len
                seen[num + right] = current_len

        return max_len

        
        

