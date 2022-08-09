from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = math.ceil(sum(piles)/h)
        right = max(piles) + 1
        while left < right:
            mid = left + (right -left) // 2
            if self.can_eat_all(piles, h, mid):
                right = mid
            else:
                left = mid + 1

        return left

    def can_eat_all(self, piles: List[int], h: int, speed: int) -> bool:
        hour = 0
        for bananas in piles:
            hour += math.ceil(bananas / speed)
        return hour <= h