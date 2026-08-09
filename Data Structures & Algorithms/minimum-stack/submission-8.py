# class MinStack:

#     def __init__(self):
#         self.stack = []
#         self.min_val = float('inf')
        
#     def push(self, val: int) -> None:
#         self.stack.append(int(val))
#         self.min_val = int(min(self.stack))

#     def pop(self) -> None:
#         if len(self.stack) > 0:
#             del self.stack[-1]
#             self.min_val = int([0 if len(self.stack) == 0 else min(self.stack)][0])

#     def top(self) -> int:
#         if len(self.stack) > 0:
#             top = self.stack[-1]
#             self.min_val = int([0 if len(self.stack) == 0 else min(self.stack)][0])
#             return top
#         return 0

#     def getMin(self) -> int:
#         return self.min_val


class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []  # Auxiliary stack to keep track of minimum values

    def push(self, val: int) -> None:
        self.stack.append(val)
        # Push the new minimum onto the min_stack
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.stack:
            if self.stack[-1] == self.min_stack[-1]:
                self.min_stack.pop()  # Pop from min_stack if it matches the popped element
            self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        return None  # Handle empty stack case if needed

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]
        return None  # Handle empty stack case if needed