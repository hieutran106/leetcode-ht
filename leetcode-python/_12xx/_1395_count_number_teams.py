import unittest
from typing import List


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        ans = 0
        for i in range(1, len(rating) - 1):
            leftLess, leftGreater = 0, 0
            rightLess, rightGreater = 0 , 0
            for j in range(0, i):
                if rating[j] < rating[i]:
                    leftLess += 1
                else:
                    leftGreater += 1
            for k in range(i+1, len(rating)):
                if rating[k] < rating[i]:
                    rightLess += 1
                else:
                    rightGreater += 1
            ans += leftLess * rightGreater + leftGreater * rightLess

        return ans

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        actual = self.s.numTeams(rating=[2, 5, 3, 4, 1])
        self.assertEqual(3, actual)

    def test_case_2(self):
        actual = self.s.numTeams(rating=[2, 1, 3])
        self.assertEqual(0, actual)

    def test_case_3(self):
        actual = self.s.numTeams(rating=[1, 2, 3, 4])
        self.assertEqual(4, actual)

    def test_case_4(self):
        actual = self.s.numTeams(rating=[20, 50, 30, 1, 40, 2, 3])
        # (20, 30, 40) (1, 2, 3)
        # (50, 30, 1) (50, 30, 2) (50, 30, 3)
        # (50, 40, 2) (50, 40, 3)
        self.assertEqual(2 + 3 + 2, actual)

    def test_case_5(self):
        actual = self.s.numTeams(rating=[1, 2, 3, 4, 100, 5, 6])
        self.assertEqual(26, actual)

    def test_case_6(self):
        actual = self.s.numTeams(rating=[1, 2, 10, 4, 3])
        self.assertEqual(4, actual)


if __name__ == '__main__':
    unittest.main()
