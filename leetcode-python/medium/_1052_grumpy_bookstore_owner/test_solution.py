import unittest
from typing import List


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:

        base = 0 #
        more = 0

        for i in range(len(customers)):
            if grumpy[i] == 0:
                base += customers[i]
            if i < minutes and grumpy[i] == 1:
                more += customers[i]
        max_more = more
        for i in range(1, len(customers) - minutes + 1):

            if grumpy[i-1] == 1:
                more -= customers[i-1]
            if grumpy[i + minutes - 1] == 1:
                more += customers[i + minutes - 1]
            print(f"At {i=}, {more=}")
            if more > max_more:
                max_more = more

        return base + max_more




class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        actual = self.s.maxSatisfied(customers=[1, 0, 1, 2, 1, 1, 7, 5], grumpy=[0, 1, 0, 1, 0, 1, 0, 1], minutes=3)
        self.assertEqual(actual, 16)

    def test_case_2(self):
        actual = self.s.maxSatisfied(customers=[1], grumpy=[0], minutes=1)
        self.assertEqual(actual, 1)

    def test_case_3(self):
        actual = self.s.maxSatisfied(customers=[0, 0], grumpy=[0, 0], minutes=1)
        self.assertEqual(actual, 0)

    def test_case_4(self):
        actual = self.s.maxSatisfied(customers=[4,10,10], grumpy=[1,1,0], minutes=2)
        self.assertEqual(actual, 24)


if __name__ == '__main__':
    unittest.main()
