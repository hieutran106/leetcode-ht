class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len_x = len(word1)
        len_y = len(word2)

        dp = [[0 for _ in range(len_y + 1)] for _ in range(len_x + 1)]

        for i in range(len_x, -1, -1):
            for j in range(len_y, -1, -1):
                if i == len_x and j == len_y:
                    continue

                if i == len_x:
                    dp[i][j] = dp[i][j+1] + 1
                    continue

                if j == len_y:
                    dp[i][j] = dp[i+1][j] + 1
                    continue

                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    min_value = min(
                        dp[i + 1][j + 1],  # replace
                        dp[i + 1][j],  # remove char from x
                        dp[i][j + 1],  # insert char to x
                    )
                    dp[i][j] = 1 + min_value

        return dp[0][0]