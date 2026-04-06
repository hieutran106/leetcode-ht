import unittest
from typing import List

# Date: 2026-04-07
# Problem: 874 walking_robot_sim
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        ans, x, y = 0, 0, 0
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        i = 0
        obstacle_set = set([(x, y) for x,y in obstacles])
        for c in commands:
            if c == -2:
                i = (i - 1) % 4
            elif c == -1:
                i = (i + 1) %4
            else:
                for step in range(1, c + 1):
                    dx, dy = dirs[i]
                    if (x+dx, y+dy) in obstacle_set:
                        break
                    x = x + dx
                    y = y+dy
                    ans = max(ans, x*x + y*y)
        return ans


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.robotSim(commands = [4,-1,3], obstacles = [])
        self.assertEqual(25, actual)
        
    def test_case_2(self):
        actual = self.s.robotSim(commands = [4,-1,4,-2,4], obstacles = [[2,4]])
        self.assertEqual(65, actual)

    def test_case_3(self):
        actual = self.s.robotSim(commands = [6,-1,-1,6], obstacles = [[0,0]])
        self.assertEqual(36, actual)

    def test_case_4(self):
        actual = self.s.robotSim(commands = [4,-1,4,-2,4], obstacles = [[2,4], [100, 100]])
        self.assertEqual(65, actual)

if __name__ == '__main__':
    unittest.main()

