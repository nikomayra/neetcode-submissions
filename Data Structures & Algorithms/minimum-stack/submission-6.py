class MinStack:

    def __init__(self):
        self.stack = []
        self.stack_min = [math.inf]

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.stack_min[-1])
        self.stack_min.append(val)

    def pop(self) -> None:
        tmp = self.stack.pop()
        self.stack_min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack_min[-1]