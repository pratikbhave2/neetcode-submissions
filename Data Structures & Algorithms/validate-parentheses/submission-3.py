class Solution:
    def isValid(self, s: str) -> bool:
        bracket_pairs = {")": "(", "]": "[", "}": "{"}
        stack = []
        for char in s:
            if char in bracket_pairs:
                if not stack:
                    return False
                
                if bracket_pairs[char] != stack.pop():
                    return False
            else:
                stack.append(char)

        return True if not stack else False
            