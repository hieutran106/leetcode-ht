import unittest
from typing import List


class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        LIS = [1 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    LIS[i] = max(LIS[i], LIS[j] + 1)

        LDS = [1 for _ in range(len(nums))]
        for i in range(len(nums) - 2, -1, -1):
            for j in range(len(nums) - 1, i, -1):
                if nums[i] > nums[j]:
                    LDS[i] = max(LDS[i], LDS[j] + 1)
        print(LIS)
        print(LDS)
        max_mountain_length = float("-inf")
        for i in range(1, len(nums) - 1):
            if LIS[i] > 1 and LDS[i] > 1:
                max_mountain_length = max(max_mountain_length, LIS[i] + LDS[i] - 1)
        return len(nums) - max_mountain_length


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        actual = self.s.minimumMountainRemovals(nums=[1, 3, 1])
        self.assertEqual(0, actual)

    def test_case_2(self):
        actual = self.s.minimumMountainRemovals(nums=[2, 1, 1, 5, 6, 2, 3, 1])
        self.assertEqual(3, actual)

    def test_case_3(self):
        actual = self.s.minimumMountainRemovals(nums=[2, 1, 2, 3, 4, 5, 4, 3])
        self.assertEqual(1, actual)

    def test_case_4(self):
        actual = self.s.minimumMountainRemovals(nums=[100, 92, 89, 77, 74, 66, 64, 66, 64])
        self.assertEqual(6, actual)

    def test_case_5(self):
        actual = self.s.minimumMountainRemovals(nums=[1, 2, 1, 3, 4, 4])
        self.assertEqual(3, actual)


if __name__ == '__main__':
    unittest.main()
