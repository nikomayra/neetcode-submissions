class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left_k = 1
        right_k = max(piles)

        while left_k < right_k:
            mid = (left_k + right_k) // 2

            if self.canFinish(piles, h, mid):
                right_k = mid
            else:
                left_k = mid + 1
        return left_k

    def canFinish(self, piles, h, k) -> bool:
        total_time = 0
        for pile in piles:
            total_time += math.ceil(pile/k)
            if total_time > h:
                return False
        
        return total_time <= h