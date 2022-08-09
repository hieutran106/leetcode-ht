# Given a non-negative integer num,
# return the number of steps to reduce it to zero.
# If the current number is even,
#   you have to divide it by 2,
#   otherwise, you have to subtract 1 from it.

"""Simple solution."""
class Solution:
    def numberOfSteps (self, num: int) -> int:
        start = 0
        count = 0
        while (num > 0):
            if num % 2 == 0:
                num = num /2
            else:
                num = num - 1

            count = count + 1

        return count

