class Solution:
    def isValid(self, s: str) -> bool:
            stack = []
            bracketPairs = {")": "(", "}": "{", "]": "["}

            for c in s:
                if c in bracketPairs:
                    if stack and stack[-1] == bracketPairs[c]:
                        stack.pop()
                    else:
                        return False
                else:
                    stack.append(c)

            return True if len(stack) == 0 else False