# tags: monotonous stack
from typing import List

class Solution:
    def largestRectangleArea(self, arr: List[int]) -> int:
        stack = []
        left = [0] * len(arr)
        for idx, ele in enumerate(arr):
            while stack and arr[stack[-1]] > arr[idx]:
                stack.pop()
            pre_less = stack[-1] if len(stack) > 0 else -1
            left[idx] = idx - pre_less - 1
            stack.append(idx)

        stack = []
        right = [0] * len(arr)
        for idx in range(len(arr))[::-1]:
            if idx == 0:
                print()
            while stack and arr[stack[-1]] >= arr[idx]:
                stack.pop()

            next_less = stack[-1] if len(stack) > 0 else len(arr)
            right[idx] = next_less - idx - 1
            stack.append(idx)

        areas = [0] * len(arr)
        for i in range(len(arr)):
            areas[i] = arr[i] * (left[i] + right[i] + 1)

        result = max(areas)
        return result
