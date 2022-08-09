# tags: stack

class Solution:
    def isValid(self, s: str) -> bool:
        open = "([{"
        close = ")]}"

        stack = []
        for c in s:
            if c in open:
                stack.append(c)
                continue

            # handle close parentheses
            if len(stack) == 0:
                return False

            # pop element at the top of stack
            top = stack[-1]
            if c == close[open.index(top)]:
                stack.pop()
            else:
                return False

        return len(stack) == 0