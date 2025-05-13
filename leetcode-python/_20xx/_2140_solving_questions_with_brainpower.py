import unittest
from typing import List

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        memo = {}
        def dp(i:int) -> int:
            if i >= len(questions):
                return 0
            if i in memo:
                return memo[i]
            # pick current
            c1 =  questions[i][0] + dp(i + questions[i][1] + 1)
            # do not pick
            c2 = dp(i+1)
            res = max(c1, c2)
            memo[i] = res
            return res
        ans = dp(0)
        return ans

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.mostPoints(questions = [[3,2],[4,3],[4,4],[2,5]])
        self.assertEqual(5, actual)
        
    def test_case_2(self):
        actual = self.s.mostPoints(questions = [[1,1],[2,2],[3,3],[4,4],[5,5]])
        self.assertEqual(7, actual)

if __name__ == '__main__':
    unittest.main()

