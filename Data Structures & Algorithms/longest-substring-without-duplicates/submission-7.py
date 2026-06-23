class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        longest = 0
        l = 0
        seen = {}
        for r in range(len(s)):
            if s[r] in seen:
                l = max(seen[s[r]] + 1, l)
            seen[s[r]] = r
            longest = max(longest, (r-l+1))
        return longest