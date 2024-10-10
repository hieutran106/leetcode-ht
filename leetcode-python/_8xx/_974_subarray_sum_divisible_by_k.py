import collections
import unittest
from typing import List


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # start - we always have prefix sum of 0
        prefix_sum = [0]
        for n in nums:
            prefix_sum.append(n + prefix_sum[-1])
        # dictionary - key: remainder divide by k, value: number of times we see the remainder before
        d = collections.defaultdict(int)

        ans = 0
        for i, v in enumerate(prefix_sum):
            r = v % k
            if r in d:
                ans += d[r]
            d[r] += 1

        return ans


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        actual = self.s.subarraysDivByK(nums=[4, 5, 0, -2, -3, 1], k=5)
        self.assertEqual(7, actual)

    def test_case_2(self):
        actual = self.s.subarraysDivByK(nums=[5], k=9)
        self.assertEqual(0, actual)
    def test_case_3(self):
        actual = self.s.subarraysDivByK(nums=[0, 5], k=5)
        self.assertEqual(3, actual)
    def test_case_4(self):
        actual = self.s.subarraysDivByK(nums=[0, 0, 5], k=5)
        self.assertEqual(6, actual)


if __name__ == '__main__':
    unittest.main()
