import unittest
from typing import List


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def time_to_int(timeStr: str):
            time_array = timeStr.split(":")
            hour = int(time_array[0])
            minute = int(time_array[1])
            return hour * 60 + minute

        values = []
        for t in timePoints:
            v = time_to_int(t)
            values.append(v)
        values.sort()
        ans = float("inf")
        for i in range(1, len(values)):
            ans = min(ans, abs(values[i] - values[i-1]))
        ans = min(ans, values[0] + 24*60 - values[-1])
        return ans


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.findMinDifference(timePoints = ["23:59","00:00"])
        self.assertEqual(1, actual)
        
    def test_case_2(self):
        actual = self.s.findMinDifference(timePoints=["00:00","23:59","00:00"])
        self.assertEqual(0, actual)

    def test_case_3(self):
        actual = self.s.findMinDifference(timePoints=["00:05","23:59","01:01", "01:10", "01:02"])
        self.assertEqual(1, actual)

    def test_case_4(self):
        actual = self.s.findMinDifference(timePoints=["12:12","00:13"])
        self.assertEqual(719, actual)

if __name__ == '__main__':
    unittest.main()

