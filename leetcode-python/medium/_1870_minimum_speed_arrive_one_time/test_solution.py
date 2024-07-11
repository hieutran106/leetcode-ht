import math
import unittest
from typing import List


class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        n = len(dist)
        if hour <= n - 1:
            return -1

        def can_arrive(speed: int):
            time = 0
            for d in dist[:n - 1]:
                time += math.ceil(d / speed)
            # last train
            time += dist[-1] / speed
            return time <= hour

        low = 1
        high = 10 ** 7
        while low < high:
            mid = low + (high - low) // 2
            if can_arrive(mid):
                high = mid
            else:
                low = mid + 1
        return low


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        actual = self.s.minSpeedOnTime(dist=[1, 3, 2], hour=6)
        self.assertEqual(actual, 1)

    def test_case_2(self):
        actual = self.s.minSpeedOnTime(dist=[1, 3, 2], hour=2.7)
        self.assertEqual(actual, 3)

    def test_case_3(self):
        actual = self.s.minSpeedOnTime(dist=[1, 3, 2], hour=1.9)
        self.assertEqual(actual, -1)

    def test_case_4(self):
        actual = self.s.minSpeedOnTime(dist=[1, 1, 1, 1000], hour=4)
        self.assertEqual(actual, 1000)

    def test_case_5(self):
        actual = self.s.minSpeedOnTime(dist=[1, 1, 1, 1000], hour=3)
        self.assertEqual(actual, -1)

    def test_case_6(self):
        actual = self.s.minSpeedOnTime(dist=[2, 6, 2], hour=5.1)
        self.assertEqual(actual, 2)

    def test_case_7(self):
        actual = self.s.minSpeedOnTime(dist=[1, 1, 100_000], hour=2.01)
        self.assertEqual(actual, 10_000_000)


if __name__ == '__main__':
    unittest.main()
