import unittest
from typing import List

# Date: 2025-09-25
# Problem: 120 triangle
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = {}
        def dp(r, c):
            if r == len(triangle) - 1:
                return triangle[r][c]
            if (r,c) in memo:
                return memo[(r, c)]
            res = min(triangle[r][c] + dp(r+1,c), triangle[r][c] + dp(r+1,c+1))
            memo[(r,c)] = res
            return res
        return dp(0, 0)


s = Solution()
class MyTestCase(unittest.TestCase):

    def test_case_1(self):
        actual = s.minimumTotal(triangle = [[2],[3,4],[6,5,7],[4,1,8,3]])
        self.assertEqual(11, actual)
        
    def test_case_2(self):
        actual = s.minimumTotal(triangle = [[-10]])
        self.assertEqual(-10, actual)

    def test_case_3(self):
        actual = s.minimumTotal(triangle = [[1], [2, 3]])
        self.assertEqual(3, actual)

if __name__ == '__main__':
    unittest.main()

