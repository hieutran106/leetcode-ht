import unittest
from typing import List

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        colors = colors + colors
        ans = 0
        for i in range(n):
            same_color = False
            for j in range(i, i+k -1):
                if colors[j] == colors[j+1]:
                    same_color = True
                    break
            if not same_color:
                ans += 1
        return ans
class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.numberOfAlternatingGroups(colors = [0,1,0,1,0], k = 3)
        self.assertEqual(3, actual)
        
    def test_case_2(self):
        actual = self.s.numberOfAlternatingGroups(colors = [0,1,0,0,1,0,1], k = 6)
        self.assertEqual(2, actual)
    def test_case_3(self):
        actual = self.s.numberOfAlternatingGroups(colors = [1,1,0,1], k = 4)
        self.assertEqual(0, actual)

if __name__ == '__main__':
    unittest.main()

