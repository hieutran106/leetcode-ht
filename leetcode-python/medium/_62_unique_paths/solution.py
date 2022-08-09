class Solution:
    """
    m = 2, n = 3
    dp table
    1 1 1 (values in top row is 1)
    1 2 3

    (all values in left most colum is 1)
    """
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 or j ==0:
                    memo[i][j] = 1
                    continue
                top = memo[i-1][j] if i-1 >= 0 else 0
                left = memo[i][j-1] if j -1 >=0 else 0
                memo[i][j] = top + left
        return memo[m-1][n-1]
