class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        num_freq = defaultdict(int)

        for num in nums:
            num_freq[num] += 1

        s_num_freq = dict(sorted(num_freq.items(), key=lambda x: x[1], reverse=True))
        
        output = []
        for i, n in enumerate(s_num_freq):
            output.append(n)
            if i == k-1:
                return output
