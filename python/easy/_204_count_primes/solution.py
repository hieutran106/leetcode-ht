class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        # Assume every number is a prime
        dp = [True] * n

        dp[0] = False
        dp[1] = False

        for i in range(2, n):
            if dp[i]:
                # mark forward
                for j in range(i*i, n, i):
                    dp[j] = False

        return sum(dp)

