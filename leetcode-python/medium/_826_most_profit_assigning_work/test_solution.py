import unittest
from typing import List


class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        difficulty.append(0)
        profit.append(0)
        sorted_tasks = sorted(zip(difficulty, profit)) # (difficulty, profit)
        rows = 3
        cols = len(difficulty)
        maxProfits = [[0 for _ in range(cols)] for _ in range(rows)]
        for i, value in enumerate(sorted_tasks):
            if i == 0:
                continue
            (d, p) = value
            maxProfits[0][i] = d
            maxProfits[1][i] = p
            maxProfits[2][i] = max(p, maxProfits[2][i-1])

        print(maxProfits)
        worker.sort()
        p = 0
        res = 0
        for w in worker:
            while p < cols and maxProfits[0][p] <= w:
                p += 1
            res += maxProfits[2][p-1]

        return res;




class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        actual = self.s.maxProfitAssignment(difficulty=[2, 4, 6, 8, 10], profit=[10, 20, 30, 40, 50],
                                            worker=[4, 5, 6, 7])
        self.assertEqual(100, actual)

    def test_case_2(self):
        actual = self.s.maxProfitAssignment(difficulty=[85, 47, 57], profit=[24, 66, 99], worker=[40, 25, 25])
        self.assertEqual(0, actual)

    def test_case_3(self):
        actual = self.s.maxProfitAssignment(difficulty=[2, 4, 6, 8, 10], profit=[50, 40, 30, 20, 10],
                                            worker=[4, 5, 6, 7])
        self.assertEqual(200, actual)

    def test_case_4(self):
        actual = self.s.maxProfitAssignment(difficulty=[68, 35, 52, 47, 86], profit=[67, 17, 1, 81, 3],
                                            worker=[92, 10, 85, 84, 82])
        self.assertEqual(324, actual)


if __name__ == '__main__':
    unittest.main()
