from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        sum = 0
        for i in range(n):
            for j in range(n):
                primary_diagonal = i == j
                secondary_diagonal = i + j == n -1
                if primary_diagonal or secondary_diagonal:
                    sum += mat[i][j]

        return sum