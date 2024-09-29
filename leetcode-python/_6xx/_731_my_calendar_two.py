import unittest
from typing import List
import collections

class MyCalendarTwo:

    def __init__(self):
        self.events = collections.defaultdict(int)

    def book(self, start: int, end: int) -> bool:
        self.events[start] += 1
        self.events[end] -= 1
        ongoing_event_count = 0
        for time in sorted(self.events):
            # the number of events at a given time
            ongoing_event_count += + self.events[time]
            if ongoing_event_count > 2:
                # revert
                self.events[start] -= 1
                self.events[end] += 1
                return False
        return True


class MyTestCase(unittest.TestCase):

    def test_case_1(self):
        cal = MyCalendarTwo()
        actual = cal.book(10, 20)
        self.assertEqual(True, actual)
        actual = cal.book(50, 60)
        self.assertEqual(True, actual)

        actual = cal.book(10, 40)
        self.assertEqual(True, actual)

        actual = cal.book(5, 15)
        self.assertEqual(False, actual)

        actual = cal.book(5, 10)
        self.assertEqual(True, actual)

        actual = cal.book(25, 55)
        self.assertEqual(True, actual)

    def test_case_2(self):
        pass


if __name__ == '__main__':
    unittest.main()
