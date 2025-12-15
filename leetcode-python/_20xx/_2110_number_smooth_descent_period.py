import unittest
from typing import List

# Date: 2025-12-15
# Problem: 2110 number_smooth_descent_period
class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        l, r, n = 0, 0, len(prices)
        ans = 0
        while l < n:
            r += 1
            if r < n and prices[r] == prices[r-1] - 1:
                continue
            d = r - l
            print(f"{r=}, {l=}, {d=}")
            ans += d * (d+1)//2
            l = r

        return ans
    

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.getDescentPeriods(prices = [3,2,1,4])
        self.assertEqual(7, actual)
        
    def test_case_2(self):
        actual = self.s.getDescentPeriods(prices = [8,6,7,7])
        self.assertEqual(4, actual)

    def test_case_3(self):
        actual = self.s.getDescentPeriods(prices = [1])
        self.assertEqual(1, actual)

if __name__ == '__main__':
    unittest.main()

