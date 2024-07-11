import unittest
from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        odd_count = 0
        l, m = 0, 0 # left and middle pointer ( 3 pointer sliding window)
        ans = 0
        for r in range(len(nums)):
            if nums[r] %2 == 1:
                odd_count += 1

            if odd_count > k:
                odd_count = odd_count - 1
                # shift the window
                l = m + 1
                m = l

            if odd_count == k:
                # update answer
                while nums[m] % 2 == 0:
                    m += 1
                ans += (m - l + 1)

        return ans








class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        actual = self.s.numberOfSubarrays(nums=[1, 1, 2, 1, 1], k=3)
        self.assertEqual(actual, 2)

    def test_case_2(self):
        actual = self.s.numberOfSubarrays(nums=[2, 4, 6], k=1)
        self.assertEqual(actual, 0)

    def test_case_3(self):
        actual = self.s.numberOfSubarrays(nums=[2, 2, 2, 1, 2, 2, 1, 2, 2, 2], k=2)
        self.assertEqual(actual, 16)

    def test_case_4(self):
        actual = self.s.numberOfSubarrays(nums=[1, 3, 5], k=1)
        self.assertEqual(actual, 3)

    def test_case_5(self):
        actual = self.s.numberOfSubarrays(nums=[1], k=1)
        self.assertEqual(actual, 1)

    def test_case_6(self):
        actual = self.s.numberOfSubarrays(nums=[2,2,1,2,1,1], k = 2);
        self.assertEqual(actual, 5)

    def test_case_7(self):
        actual = self.s.numberOfSubarrays(nums=[0, 0, 1, 1, 0, 0, 0], k=2);
        self.assertEqual(actual, 12)


if __name__ == '__main__':
    unittest.main()
