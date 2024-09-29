import unittest
from typing import List


def is_overlap(i1, i2):
    start1, end1 = i1
    start2, end2 = i2
    overlap = start1 <= start2 < end1 or start2<=start1 < end2
    return overlap


class MyCalendar:

    def __init__(self):
        self.booking = []

    def book(self, start: int, end: int) -> bool:
        for interval in self.booking:
            if is_overlap(interval, (start, end)):
                return False
        self.booking.append((start, end))
        self.booking.sort()
        return True


class MyTestCase(unittest.TestCase):

    def test_case_1(self):
        cal = MyCalendar()
        actual = cal.book(10, 20)
        self.assertEqual(True, actual)
        actual = cal.book(15, 25)
        self.assertEqual(False, actual)
        actual = cal.book(20, 30)
        self.assertEqual(True, actual)

    def test_case_2(self):
        pass


if __name__ == '__main__':
    unittest.main()
