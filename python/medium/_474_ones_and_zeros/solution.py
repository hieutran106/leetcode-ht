from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:

        num_items = len(strs)

        dict = self.count(strs)
        dp = [[[0] * (n+1) for _ in range(m+1)] for _ in range(num_items+1)]

        for i in range(1, num_items+1):
            for j in range(0, m+1):
                for k in range(0, n+1):
                    item = strs[i-1]
                    (m_current, n_current) = dict[item]
                    # if not pick i-th item
                    value1 = dp[i-1][j][k]

                    # pick item i-th
                    value2 = 0
                    if m_current <=j and n_current <=k:
                        value2 = 1 + dp[i-1][j-m_current][k-n_current]

                    dp[i][j][k] = max(value1, value2)

        return dp[num_items][m][n]

    def count(self, strs):
        dict = {}
        for w in strs:
            m = w.count('0')
            n = w.count('1')
            dict[w] = (m, n)
        return dict

