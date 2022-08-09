class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        for char in s:
            if char == "(":
                stack.append(char)
            else:
                if len(stack) == 0:
                    stack.append(char)
                    continue

                top = stack[len(stack) - 1]
                if top == "(":
                    stack.pop()
                else:
                    stack.append(char)

        return len(stack)