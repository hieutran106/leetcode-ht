import unittest
from typing import List

# Date: 2026-08-06
# Problem: 3345 smallest_divisible_digit_product
class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def product_digit(n):
            res = 1
            while n > 0:
                res = res * (n % 10)
                n = n // 10
            return res
        for i in range(n, n + 10):
            product = product_digit(i)
            if product % t == 0:
                return i
        return None
    

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.smallestNumber(n = 10, t = 2)
        self.assertEqual(actual, 10)
        
    def test_case_2(self):
        actual = self.s.smallestNumber(n = 15, t = 3)
        self.assertEqual(actual, 16)

if __name__ == '__main__':
    unittest.main()

