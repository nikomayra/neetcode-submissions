class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for point in points:
            dist_squared = point[0]**2 + point[1]**2
            distances.append((dist_squared, point))
        
        distances.sort()
        return [point for _, point in distances[:k]]