class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == '+':
                operand = stack.pop()
                res = stack.pop()
                stack.append(res + operand)
            elif token == '-':
                operand = stack.pop()
                res = stack.pop()
                stack.append(res - operand)
            elif token == '*':
                operand = stack.pop()
                res = stack.pop()
                stack.append(res * operand)
            elif token == '/':
                operand = stack.pop()
                res = stack.pop()
                stack.append(int(res / operand))
            else:
                stack.append(int(token))
            
        return stack[0]