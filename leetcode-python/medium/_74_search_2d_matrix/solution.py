from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])

        start = 0
        end = n * m

        return self.helper(matrix, m, n, target, start, end)

    def helper(self, matrix, m, n, target, start, end):
        if end <= start:
            return False
        mid = (start + end) // 2

        row = mid // m
        col = mid % m
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            return self.helper(matrix, m, n, target, mid + 1, end)
        else:
            return self.helper(matrix, m, n, target, start, mid)

