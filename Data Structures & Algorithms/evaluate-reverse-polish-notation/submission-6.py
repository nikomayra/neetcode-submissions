class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == '+':
                operand = int(stack.pop())
                res = int(stack.pop())
                stack.append(res + operand)
            elif token == '-':
                operand = int(stack.pop())
                res = int(stack.pop())
                stack.append(res - operand)
            elif token == '*':
                operand = int(stack.pop())
                res = int(stack.pop())
                stack.append(res * operand)
            elif token == '/':
                operand = int(stack.pop())
                res = int(stack.pop())
                stack.append(int(res / operand))
            else:
                stack.append(token)
            
        return int(stack[0])