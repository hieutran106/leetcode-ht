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
        return sum
