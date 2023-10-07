import unittest
from .solution import Solution
from typing import List


class Solution:
    def divisorGame(self, n: int) -> bool:
        return True if n %2 ==0 else False

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.divisorGame(n=2)
        self.assertEqual(True, actual)
        
    def test_case_2(self):
        actual = self.s.divisorGame(n=3)
        self.assertEqual(False, actual)

if __name__ == '__main__':
    unittest.main()

