# We need to search for maximal k satisfying k^2 <= x
class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        while left < right:
            mid = left + (right - left) // 2 + 1
            if mid * mid > x:
                right = mid - 1
            else:
                left = mid

        return left


