import unittest
from typing import List

#2025-12-06
class StockSpanner:

    def __init__(self):
        # decreasing stack (stock_value, span_for_that_day)
        self.s = []
    def next(self, price: int) -> int:
        count = 1
        while self.s and price >= self.s[-1][0]:
            # accumulate the count and pop lower price from the stack
            count += self.s[-1][1]
            self.s.pop()
        self.s.append((price, count))
        return count

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = StockSpanner()
    
    def test_case_1(self):
        ans = self.s.next(100)
        self.assertEqual(1, ans)

        ans = self.s.next(80)
        self.assertEqual(1, ans)

        ans = self.s.next(60)
        self.assertEqual(1, ans)

        ans = self.s.next(70)
        self.assertEqual(2, ans)

        ans = self.s.next(60)
        self.assertEqual(1, ans)

        ans = self.s.next(75)
        self.assertEqual(4, ans)

    def test_case_2(self):
        ans = self.s.next(100)
        self.assertEqual(1, ans)

        ans = self.s.next(80)
        self.assertEqual(1, ans)

        ans = self.s.next(60)
        self.assertEqual(1, ans)

        ans = self.s.next(70)
        self.assertEqual(2, ans)

        ans = self.s.next(60)
        self.assertEqual(1, ans)

        ans = self.s.next(75)
        self.assertEqual(4, ans)

        ans = self.s.next(85)
        self.assertEqual(6, ans)


if __name__ == '__main__':
    unittest.main()

