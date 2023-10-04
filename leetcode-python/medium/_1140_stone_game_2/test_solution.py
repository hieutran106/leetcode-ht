import unittest
from .solution import Solution
from typing import List


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        return 0

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.stoneGameII(piles = [2,7,9,4,4])
        self.assertEqual(10, actual)
        
    def test_case_2(self):
        actual = self.s.stoneGameII(piles = [1,2,3,4,5,100])
        self.assertEqual(104, actual)

if __name__ == '__main__':
    unittest.main()

