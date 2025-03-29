import unittest
from typing import List


class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        dpMax = [0] * len(nums)
        dpMin = [0] * len(nums)
        dpMax[0] = nums[0]
        dpMin[0] = nums[0]
        for i in range(1, len(nums)):
            dpMax[i] = max(dpMax[i - 1] + nums[i], nums[i])
            dpMin[i] = min(dpMin[i - 1] + nums[i], nums[i])

        print(f"{dpMax=}")
        print(f"{dpMin=}")

        ans1 = max(dpMax)
        ans2 = min(dpMin)
        return max(abs(ans1), abs(ans2))


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        actual = self.s.maxAbsoluteSum(nums=[1, -3, 2, 3, -4])
        self.assertEqual(5, actual)

    def test_case_2(self):
        actual = self.s.maxAbsoluteSum(nums=[2, -5, 1, -4, 3, -2])
        self.assertEqual(8, actual)

    def test_case_3(self):
        actual = self.s.maxAbsoluteSum(nums=[1, -3, 2, -4])
        self.assertEqual(5, actual)


if __name__ == '__main__':
    unittest.main()
