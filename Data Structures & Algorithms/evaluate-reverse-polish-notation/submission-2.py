class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            if self.isOperator(c):
                b = int(stack.pop())
                a = int(stack.pop())
                result = self.apply_operator(c, a, b)
                stack.append(result)
            else:
                stack.append(int(c))
            # while len(stack) != 0:
        return int(stack.pop())

    def isOperator(self, operand: str) -> bool:
        return operand in ["+", "-", "*", "/"]
    
    def apply_operator(self, operand: str, a: int, b: int) -> int:
        if operand == "+":
            return a + b
        elif operand == "-":
            return a - b
        elif operand == "*":
            return a * b
        elif operand == "/":
            return a / b
        else:
            raise ValueError(f"Unsupported operand: {operand}")

