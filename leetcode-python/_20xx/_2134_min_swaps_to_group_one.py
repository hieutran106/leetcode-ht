import unittest
from typing import List


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        """
        Count the number of 1: one_count
        For each window of size one_count, count the number of zero - zero_count
        The number of zero is the number of swap needed
        To eliminate the circular property, we can append the original array to itself
        """
        one_count = nums.count(1)
        nums.extend(nums)
        zero_count = nums[:one_count].count(0)
        ans = zero_count
        for i in range(1, len(nums) - one_count):
            if nums[i - 1] == 0:
                zero_count -= 1
            if nums[i - 1 + one_count] == 0:
                zero_count += 1
            ans = min(ans, zero_count)
        return ans


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        actual = self.s.minSwaps(nums=[0, 1, 0, 1, 1, 0, 0])
        self.assertEqual(1, actual)

    def test_case_2(self):
        actual = self.s.minSwaps(nums=[0, 1, 1, 1, 0, 0, 1, 1, 0])
        self.assertEqual(2, actual)

    def test_case_3(self):
        actual = self.s.minSwaps(nums=[1, 1, 0, 0, 1])
        self.assertEqual(0, actual)

    def test_case_4(self):
        actual = self.s.minSwaps(nums=[1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0])
        self.assertEqual(1, actual)

    def test_case_5(self):
        actual = self.s.minSwaps(nums=[1])
        self.assertEqual(0, actual)


if __name__ == '__main__':
    unittest.main()
