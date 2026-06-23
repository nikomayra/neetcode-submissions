class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def is_palindrome(string):
            return string == string[::-1]
    
        def backtrack(start):
            if start >= len(s):
                res.append(current.copy())
                return

            for end in range(start, len(s)):
                substring = s[start:end+1]
                if is_palindrome(substring):
                    current.append(substring)
                    backtrack(end + 1)
                    current.pop()

        res = []
        current = []
        backtrack(0)
        return res