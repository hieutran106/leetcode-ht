import unittest
from .solution import Solution
from typing import List


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        laser_count = 0
        prev = None
        for r in bank:
            one_count = 0
            for c in r:
                if c == '1':
                    one_count += 1
            if one_count == 0:
                continue
            if prev == None:
                prev = one_count
                continue
            laser_count += one_count * prev
            prev = one_count
        return laser_count


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        actual = self.s.numberOfBeams(bank=["011001", "000000", "010100", "001000"])
        self.assertEqual(8, actual)

    def test_case_2(self):
        actual = self.s.numberOfBeams(bank=["000", "111", "000"])
        self.assertEqual(0, actual)


if __name__ == '__main__':
    unittest.main()
