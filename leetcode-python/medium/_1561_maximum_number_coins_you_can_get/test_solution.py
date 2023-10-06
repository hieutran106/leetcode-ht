import unittest
from .solution import Solution
from typing import List


class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n = len(piles) // 3
        piles.sort()
        piles = piles[n:]
        print(piles)
        total = 0
        for i in range(0, len(piles), 2):
            total += piles[i]

        return total
class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.maxCoins(piles = [2,4,1,2,7,8])
        self.assertEqual(9, actual)
        
    def test_case_2(self):
        actual = self.s.maxCoins(piles=[2,4,5])
        self.assertEqual(4, actual)

    def test_case_2(self):
        actual = self.s.maxCoins(piles = [9,8,7,6,5,1,2,3,4])
        self.assertEqual(18, actual)

if __name__ == '__main__':
    unittest.main()

