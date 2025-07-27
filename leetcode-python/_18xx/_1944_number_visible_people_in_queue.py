import unittest
from typing import List

# Date: 2025-03-07
class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        # traverse from Right to Left, using decreasing stack
        ans = [0] * len(heights)
        stack = []
        for i, h in enumerate(reversed(heights)):
            while stack and h > stack[-1]:
                stack.pop()
                ans[i] += 1
            if stack: # last person cannot see
                ans[i] += 1
            stack.append(h)

        return list(reversed(ans))
    

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.canSeePersonsCount(heights = [10,6,8,5,11,9])
        self.assertEqual([3,1,2,1,1,0], actual)
        
    def test_case_2(self):
        actual = self.s.canSeePersonsCount(heights = [5,1,2,3,10])
        self.assertEqual([4,1,1,1,0], actual)

    def test_case_3(self):
        actual = self.s.canSeePersonsCount(heights = [10, 1, 2, 3, 1, 9])
        self.assertEqual([4,1,1,2,1,0], actual)

    def test_case_4(self):
        actual = self.s.canSeePersonsCount(heights = [1, 2, 3])
        self.assertEqual([1, 1, 0], actual)

    def test_case_5(self):
        actual = self.s.canSeePersonsCount(heights = [3, 2, 1])
        self.assertEqual([1, 1, 0], actual)

if __name__ == '__main__':
    unittest.main()

