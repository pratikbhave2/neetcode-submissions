class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if self.isOperator(token):
                b = stack.pop()
                a = stack.pop()
                res = self.applyOperator(a, b, token)
                stack.append(res)
            else:
                stack.append(int(token))

        return stack[-1]

    def isOperator(self, s: str) -> bool:
        return s in ["+", "-", "*", "/"]

    def applyOperator(self, a: int, b: int, operator: str) -> int:
        if operator == "+":
            return a + b
        elif operator == "*":
            return a * b
        elif operator == "/":
            return int(a / b)
        elif operator == "-":
            return a - b
        else:
            raise ValueError(f"Unsupported operand: {operand}")
        
