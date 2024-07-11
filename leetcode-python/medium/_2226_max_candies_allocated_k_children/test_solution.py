import unittest
from typing import List


class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        return 0


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        actual = self.s.maximumCandies(candies=[5, 8, 6], k=3)
        self.assertEqual(actual, 5)

    def test_case_2(self):
        actual = self.s.maximumCandies(candies=[3, 6, 15], k=2)
        self.assertEqual(actual, 7)

    def test_case_3(self):
        actual = self.s.maximumCandies(candies=[2, 5], k=11)
        self.assertEqual(actual, 0)


if __name__ == '__main__':
    unittest.main()
