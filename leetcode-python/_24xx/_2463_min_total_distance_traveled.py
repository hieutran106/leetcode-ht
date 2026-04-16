import unittest
from typing import List

# Date: 2026-04-14
# Problem: 2463 min_total_distance_traveled
class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        pass

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.minimumTotalDistance(robot = [0,4,6], factory = [[2,2],[6,2]])
        self.assertEqual(4, actual)
        
    def test_case_2(self):
        actual = self.s.minimumTotalDistance(robot = [1,-1], factory = [[-2,1],[2,1]])
        self.assertEqual(2, actual)

    def test_case_3(self):
        actual = self.s.minimumTotalDistance(robot = [0,5,6], factory = [[2,2],[6,2]])
        self.assertEqual(3, actual)

if __name__ == '__main__':
    unittest.main()

