class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        pairs = [(freq, num) for num, freq in count.items()]
        pairs.sort(reverse=True)
        return [num for freq, num in pairs[:k]]