from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:


        left = weights[0]
        right = sum(weights) + 1

        while left < right - 2:
            mid = left + (right -left) // 2
            if self.can_shipped(weights, days, capacity=mid):
                right = mid + 1
            else:
                left = mid + 1

        return left

    def can_shipped(self, weights: List[int], days: int, capacity: int):
        day = 1
        total = 0
        for weight in weights:
            if total + weight <= capacity:
                total += weight
            elif weight <= capacity:
                total = weight
                day += 1
            else:
                return False

        return day <= days
