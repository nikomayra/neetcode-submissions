class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prod = 1
        zero_count = 0
        output = [0]*len(nums)

        for num in nums:
            if num == 0:
                zero_count += 1
            else:
                prod *= num
        if zero_count > 1:
            return output
            
        for i, num in enumerate(nums):
            if zero_count == 1:
                output[i] = 0 if num != 0 else prod
            else:
                output[i] = prod // num
        
        return output