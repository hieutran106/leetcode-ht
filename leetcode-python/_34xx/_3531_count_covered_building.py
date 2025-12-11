import unittest
from typing import List

# Date: 2025-12-12
# Problem: 3531 count_covered_building
class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        # find min and max for each row and col
        # 0 unuse
        rows = [{"min": float("inf"), "max": float("-inf")} for _ in range(n+1)]
        cols = [{"min": float("inf"), "max": float("-inf")} for _ in range(n+1)]
        for x, y in buildings:
            rows[x]["min"] = min(rows[x]["min"], y)
            rows[x]["max"] = max(rows[x]["max"], y)

            cols[y]["min"] = min(cols[y]["min"], x)
            cols[y]["max"] = max(cols[y]["max"], x)

        ans = 0
        for x, y in buildings:
            if rows[x]["min"] < y < rows[x]["max"] and cols[y]["min"] < x < cols[y]["max"]:
                ans += 1
        return ans
    

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.countCoveredBuildings(n = 3, buildings = [[1,2],[2,2],[3,2],[2,1],[2,3]])
        self.assertEqual(1, actual)
        
    def test_case_2(self):
        actual = self.s.countCoveredBuildings(n = 3, buildings = [[1,1],[1,2],[2,1],[2,2]])
        self.assertEqual(0, actual)

    def test_case_3(self):
        actual = self.s.countCoveredBuildings(n = 5, buildings = [[1,3],[3,2],[3,3],[3,5],[5,3]])
        self.assertEqual(1, actual)

    def test_case_4(self):
        actual = self.s.countCoveredBuildings(n = 3, buildings = [[1,2]])
        self.assertEqual(0, actual)

    def test_case_5(self):
        actual = self.s.countCoveredBuildings(n = 4, buildings = [[2,4],[1,2],[3,1],[1,4],[2,3],[3,3],[2,2],[1,3]])
        self.assertEqual(1, actual)

if __name__ == '__main__':
    unittest.main()

