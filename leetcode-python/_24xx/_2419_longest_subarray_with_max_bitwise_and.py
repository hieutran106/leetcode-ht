import unittest
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_and = max(nums)
        ans = 1
        count = 0
        for n in nums:
            if n == max_and:
                count += 1
            else:
                count = 0
            ans = max(ans, count)
        return ans


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        actual = self.s.longestSubarray(nums=[1, 2, 3, 3, 2, 2])
        self.assertEqual(2, actual)

    def test_case_2(self):
        actual = self.s.longestSubarray(nums=[1, 2, 3, 4])
        self.assertEqual(1, actual)

    def test_case_3(self):
        actual = self.s.longestSubarray(nums=[1, 2, 3, 3, 3, 0, 2, 3, 3, 3, 3, 3, 3, 1])
        self.assertEqual(6, actual)


if __name__ == '__main__':
    unittest.main()
