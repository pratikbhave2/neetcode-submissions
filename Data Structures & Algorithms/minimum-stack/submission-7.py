class MinStack:

    def __init__(self):
        self.stack = []
        self.min_val = float('inf')
        
    def push(self, val: int) -> None:
        self.stack.append(int(val))
        self.min_val = int(min(self.stack))

    def pop(self) -> None:
        if len(self.stack) > 0:
            del self.stack[-1]
            self.min_val = int([0 if len(self.stack) == 0 else min(self.stack)][0])

    def top(self) -> int:
        if len(self.stack) > 0:
            top = self.stack[-1]
            self.min_val = int([0 if len(self.stack) == 0 else min(self.stack)][0])
            return top
        return 0

    def getMin(self) -> int:
        return self.min_val
