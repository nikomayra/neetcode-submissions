class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        digit_hash = {
            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz',
        }

        def backtrack(digits_index):
            if len(current) == len(digits):
                res.append(''.join(current.copy()))
                return
            for letter in digit_hash[digits[digits_index]]:
                current.append(letter)
                backtrack(digits_index + 1)
                current.pop()
            
        res = []
        current = []
        backtrack(0)
        return res

        