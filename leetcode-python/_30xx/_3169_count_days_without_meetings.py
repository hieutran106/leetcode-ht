import unittest
from typing import List
import collections
#2025-24-03
class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort() # sort in-place
        # merge meetings
        merged = []
        for [start, end] in meetings:
            if not merged:
                merged.append([start, end])
                continue
            last = merged[-1]
            if last[1] < start:
                merged.append(([start, end]))
            else:
                last[1] = max(end, last[1])

        meeting_count = 0
        for [start, end] in merged:
            meeting_count += end - start + 1
        return days - meeting_count



class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.countDays(days = 10, meetings = [[5,7],[1,3],[9,10]])
        self.assertEqual(2, actual)
        
    def test_case_2(self):
        actual = self.s.countDays(days = 5, meetings = [[2,4],[1,3]])
        self.assertEqual(1, actual)

    def test_case_3(self):
        actual = self.s.countDays(days = 6, meetings = [[1,6]])
        self.assertEqual(0, actual)

    def test_case_4(self):
        actual = self.s.countDays(days = 10, meetings = [[5,7],[1,3],[9,10], [1,4]])
        self.assertEqual(1, actual)

    def test_case_5(self):
        actual = self.s.countDays(days = 8, meetings = [[2,3],[3,5],[8,8]])
        self.assertEqual(3, actual)

if __name__ == '__main__':
    unittest.main()

