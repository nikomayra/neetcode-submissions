class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1

        while l < r:
            mid = (r + l) // 2

            if nums[r] > nums[mid]:
                r = mid
            elif nums[l] < nums[mid]:
                l = mid + 1
            else:
                return nums[r]
        return nums[r]