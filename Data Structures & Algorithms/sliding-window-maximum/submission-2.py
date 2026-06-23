class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        queue = deque(nums[:k])
        max_list = [max(queue)]
        for i in range(k, len(nums)):
            queue.popleft()
            queue.append(nums[i])
            max_list.append(max(queue))
        return max_list

        # Maybe?? O(n) idea
        # start = 0
        # window_max = max(nums[:k])
        # max_list = []
        # for end in range(k-1, len(nums)):
        #     exiting = nums[start]
        #     entering = nums[end]
        #     if end - start == k - 1:
        #         start += 1
        #         window_max = max(window_max, exiting, entering)
        #         max_list.append(window_max)
        # return max_list

