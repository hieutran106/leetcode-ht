# tags: binary search

class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        left = 1
        right = m * n + 1
        while left < right:
            mid = left + (right - left) // 2
            if self.is_feasible( m, n, k, mid):
                left = mid + 1
            else:
                right = mid

        return left - 1

    def is_feasible(self, m, n, k, value):
        count = 0
        for row in range(1, m + 1):
            count += min(n, (value - 1) // row)
            # early return
            if count >= k:
                return False

        return count < k






