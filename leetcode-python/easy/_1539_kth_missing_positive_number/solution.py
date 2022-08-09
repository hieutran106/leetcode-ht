from typing import List

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        current = 1
        order = 1
        idx = 0
        while (True):
            if order > k:
                return current - 1

            if (idx < len(arr) and arr[idx] == current):
                idx = idx + 1
            else:
                order = order + 1

            current = current + 1



