# tags: dp
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])

        dp = [[0 for _ in range(col)] for _ in range(row)]
        for i in range(row):
            for j in range(col):
                if i==0 and j ==0:
                    dp[i][j] = 1 if obstacleGrid[i][j] == 0 else 0
                    continue

                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                elif j == 0:
                    dp[i][j] = dp[i-1][j]
                elif i == 0:
                    dp[i][j] = dp[i][j-1]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[row-1][col-1]
