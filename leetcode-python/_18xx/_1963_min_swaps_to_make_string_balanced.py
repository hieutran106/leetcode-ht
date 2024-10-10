import unittest
from typing import List


class Solution:
    def minSwaps(self, s: str) -> int:
        return 0


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.minSwaps(s = "][][")
        self.assertEqual(1, actual)
        
    def test_case_2(self):
        actual = self.s.minSwaps(s = "]]][[[")
        self.assertEqual(2, actual)

    def test_case_3(self):
        actual = self.s.minSwaps(s = "[]")
        self.assertEqual(0, actual)

if __name__ == '__main__':
    unittest.main()

