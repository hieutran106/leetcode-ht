from typing import List


class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        if len(A) < 2:
            return True

        diff = []
        for i in range(1, len(A)):
            diff.append(A[i] - A[i - 1])

        all_positive = all([item >= 0 for item in diff])
        all_negative = all([item <= 0 for item in diff])

        return all_positive or all_negative


class Solution2:
    def isMonotonic(self, A: List[int]) -> bool:
        n= len(A)
        if n <= 2:
            return True

        is_great = False
        is_less = False
        for i in range(1, n):
            if A[i-1] > A[i]:
                is_great = True

            if A[i-1] < A[i]:
                is_less = True

            if is_great and is_less:
                return False

        return True