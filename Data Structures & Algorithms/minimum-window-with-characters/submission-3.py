class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not s or len(s) < len(t):
            return ""
        
        s_window_count = defaultdict(int)
        t_count = Counter(t)

        l= 0
        ans, ans_len = [-1, -1], float("infinity")
        match_count = 0
        
        for r in range(len(s)):
            s_window_count[s[r]] += 1
            if s[r] in t_count and s_window_count[s[r]] == t_count[s[r]]:
                match_count += 1
            while match_count == len(t_count):
                if (r - l + 1) < ans_len:
                    ans = [l, r]
                    ans_len = r - l + 1
                s_window_count[s[l]] -= 1
                if s[l] in t_count and s_window_count[s[l]] < t_count[s[l]]:
                    match_count -= 1
                l += 1
        return s[ans[0]:ans[1]+1] if ans_len != float("infinity") else ""

