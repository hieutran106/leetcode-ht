# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
def isBadVersion(version):
     pass

class Solution:
    def firstBadVersion(self, n):
        left = 1
        right = n + 1
        while left < right:
            middle = left + (right - left) // 2
            if isBadVersion(middle):
                right = middle
            else:
                left = middle + 1

        return left
