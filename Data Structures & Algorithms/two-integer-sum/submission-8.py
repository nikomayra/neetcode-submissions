class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # What nums exist, nums : [indeces], O(n)
        num_idx = {}
        for i in range(len(nums)):
            if nums[i] not in num_idx:
                num_idx[nums[i]] = []
            num_idx[nums[i]].append(i)
        
        # Does target - curr num exist in num_idx, what idx?
        for i in range(len(nums)):
            delta = target - nums[i]
            if delta in num_idx:
                j = num_idx[delta][0]
                if j == i:          # it picked itself, try the second index
                    if len(num_idx[delta]) > 1:
                        return [i, num_idx[delta][1]]
                else:
                    return [i, j]