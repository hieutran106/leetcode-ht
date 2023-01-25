from typing import List
import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        We need to search k in range [1..max(piles]
        Bruce force is one option, but we can optimize by using binary search
        """
        left = 1
        right = max(piles)
        while left <= right:
            mid = (left + right) // 2
            can_finish = self.can_finish_banana_before_guard(mid, piles, h)
            # if koko can finish, we need to search to the left to find minimum value of k
            if can_finish:
                right = mid - 1
            else:
                # koko cannot finish, need to eat at faster speed
                left = mid + 1

        return left

    def can_finish_banana_before_guard(self, speed, piles, returning_hour):
        hour = 0
        for banana in piles:
            hour += math.ceil(banana/speed)
        return hour <= returning_hour
