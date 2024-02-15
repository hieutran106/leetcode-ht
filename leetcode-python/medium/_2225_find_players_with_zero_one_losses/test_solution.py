import unittest
from typing import List
import collections

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        win_players = set()
        lost_freq = collections.defaultdict(int)

        for w,l in matches:
            win_players.add(w)
            lost_freq[l] += 1

        lost_players = set()
        lost_one = []
        for p, times in lost_freq.items():
            if times == 1:
                lost_one.append(p)
            lost_players.add(p)

        win = list(win_players - lost_players)
        win.sort()
        lost_one.sort()

        return [win, lost_one]


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        actual = self.s.findWinners(
            matches=[[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]])
        self.assertEqual(actual, [[1, 2, 10], [4, 5, 7, 8]])

    def test_case_2(self):
        actual = self.s.findWinners(
            matches=[[2, 3], [1, 3], [5, 4], [6, 4]])
        self.assertEqual(actual, [[1, 2, 5, 6], []])


if __name__ == '__main__':
    unittest.main()
