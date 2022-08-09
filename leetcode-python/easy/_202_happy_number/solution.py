def square(x: str):
    x_int = int(x)
    return x_int * x_int


class Solution:
    """
    Not happy number results in a loop 2, 4, 16, 37, 58, 89, 145, 42, 20, 4
    """
    def isHappy(self, n: int) -> bool:
        while True:
            print(n)
            digits = list(str(n))
            n = sum(map(square, digits))
            if n == 1:
                return True
            elif n == 4:
                return False
