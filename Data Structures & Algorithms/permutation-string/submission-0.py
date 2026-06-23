class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_sort = sorted(s1)
        s2_sub = deque()

        for right in range(len(s2)):
            s2_sub.append(s2[right])
            if len(s2_sub) == len(s1_sort):
                if sorted(s2_sub) == s1_sort:
                    return True
                else:
                    s2_sub.popleft()
        return False