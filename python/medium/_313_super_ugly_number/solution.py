from typing import List
import heapq

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        # dp[i] hold ugly number i-th
        dp = [1, 1]

        heap = primes.copy()

        for i in range(2, n + 1):
            min = heap[0]
            while len(heap) > 0 and heap[0] == min:
                heapq.heappop(heap)

            dp.append(min)
            for p in primes:
                heapq.heappush(heap, dp[i] * p)

        return dp[n]
