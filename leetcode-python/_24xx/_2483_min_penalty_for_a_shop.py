import unittest
from typing import List

# Date: 2025-12-27
# Problem: 2483 min_penalty_for_a_shop
class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        open_penalty = [0] * (n + 1)
        close_penalty = [0] * (n + 1)
        for i in range(1, len(open_penalty)):
            open_penalty[i] = open_penalty[i-1]
            if customers[i-1] == 'N':
                open_penalty[i] += 1

        for i in range(len(close_penalty) - 2, -1, - 1):
            close_penalty[i] = close_penalty[i+1]
            if customers[i] == 'Y':
                close_penalty[i]+= 1
        print(open_penalty)
        print(close_penalty)

        min_penalty = float("inf")
        ans = None
        for i in range(len(open_penalty)):
            penalty = open_penalty[i] + close_penalty[i]
            if penalty < min_penalty:
                min_penalty = penalty
                ans = i
        return ans

    

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.bestClosingTime(customers = "YYNY")
        self.assertEqual(2, actual)
        
    def test_case_2(self):
        actual = self.s.bestClosingTime(customers = "NNNNN")
        self.assertEqual(0, actual)

    def test_case_3(self):
        actual = self.s.bestClosingTime(customers = "YYYY")
        self.assertEqual(4, actual)

if __name__ == '__main__':
    unittest.main()

