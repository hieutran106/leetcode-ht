from typing import List


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        left = min(bloomDay)
        right = max(bloomDay) + 1
        while left < right:
            mid = left + (right-left)//2
            if self.can_make(bloomDay, m, k, mid):
                right = mid
            else:
                left = mid + 1

        if self.can_make(bloomDay, m, k, left):
            return left
        else:
            return -1



    def can_make(self, bloomDay: List[int], m: int, k: int, d: int) -> bool:
        bloom = list(map(lambda e: e <= d, bloomDay))
        bouquet_count = 0
        flower_count = 0
        for flower in bloom:
            if flower:
                flower_count += 1
                if flower_count == k:
                    bouquet_count += 1
                    flower_count = 0
            else:
                flower_count = 0

        return bouquet_count >= m
