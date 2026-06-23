class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {")" : "(", "]" : "[", "}" : "{"}

        for b in s:
            if b in bracket_map:
                if stack and stack[-1] == bracket_map[b]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(b)
        return False if stack else True
            