from typing import List


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        stack = [start]
        visited = []
        while len(stack) > 0:
            top = stack.pop()
            if arr[top] == 0:
                return True

            visited.append(top)
            # get valid next hops
            next_hops = filter(lambda x: 0 <= x < len(arr) and x not in visited, [top + arr[top], top - arr[top]])
            stack.extend(next_hops)

        return False
