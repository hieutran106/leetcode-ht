from typing import List

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        sum = 0
        M = 10 ** 9 + 7
        for i in range(n):
            # find step to the left
            left = 1
            while i - left >=0 and arr[i -left] > arr[i]:
                left += 1

            left -= 1

            right = 1
            while i + right < n and arr[i+right] >= arr[i]:
                right += 1

            right -= 1

            number = (left +1) * (right + 1)
            sum += arr[i] * number
        return sum % M

class Solution2:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        sum = 0
        mod = 10 ** 9 + 7

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
            right[idx] = next_less - idx -1
            stack.append(idx)

        for ele, left, right in zip(arr, left, right):
            sum += ele * (left+1) * (right + 1)

        return sum % mod