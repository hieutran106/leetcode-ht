class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        while n > 1:
            if n % 5 == 0:
                n = n / 5
                continue
            elif n %3 == 0:
                n = n / 3
                continue
            elif n %2 == 0:
                n = n / 2
                continue
            else:
                return False

        return True

