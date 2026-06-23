class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-1*stone for stone in stones ]
        heapq.heapify(maxHeap)
        print(maxHeap)
        while len(maxHeap) > 1:
            x = -1 * heapq.heappop(maxHeap) # Biggest
            y = -1 * heapq.heappop(maxHeap) # Second biggest
            print(x,y)
            delta = x - y
            if delta > 0:
                heapq.heappush(maxHeap, -1*delta)
        return -1*maxHeap[0] if maxHeap else 0
