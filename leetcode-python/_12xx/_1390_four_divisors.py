import unittest
from typing import List
import math
# Date: 2026-01-04
# Problem: 1390 four_divisors
class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        ans = 0
        for n in nums:
            divisor = set()
            for i in range(1, math.isqrt(n) + 1):
                if n % i == 0:
                    divisor.add(i)
                    divisor.add(n // i)
                if len(divisor) > 4:
                    break
            if len(divisor) == 4:
                ans += sum(divisor)
        return ans
    

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.sumFourDivisors(nums = [21,4,7])
        self.assertEqual(32, actual)
        
    def test_case_2(self):
        actual = self.s.sumFourDivisors(nums = [21,21])
        self.assertEqual(64, actual)

    def test_case_3(self):
        actual = self.s.sumFourDivisors(nums = [1,2,3,4,5])
        self.assertEqual(0, actual)

    def test_case_4(self):
        actual = self.s.sumFourDivisors(nums = [1,2,3,4,5,6,7,8,9,10])
        self.assertEqual(45, actual)

if __name__ == '__main__':
    unittest.main()

