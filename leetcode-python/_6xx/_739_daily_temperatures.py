import unittest
from typing import List

#2025-12-06
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        decreasing_stack = []
        for i, v in enumerate(temperatures):
            while decreasing_stack and v > decreasing_stack[-1][0]:
                smaller_tem_index = decreasing_stack[-1][1]
                ans[smaller_tem_index] = i - smaller_tem_index
                decreasing_stack.pop()
            decreasing_stack.append((v, i))
        return ans

class MyTestCase(unittest.TestCase):



    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.dailyTemperatures(temperatures = [73,74,75,71,69,72,76,73])
        self.assertEqual([1,1,4,2,1,1,0,0], actual)
        
    def test_case_2(self):
        actual = self.s.dailyTemperatures(temperatures = [30,40,50,60])
        self.assertEqual([1,1,1,0], actual)

    def test_case_3(self):
        actual = self.s.dailyTemperatures(temperatures = [30,60,90])
        self.assertEqual([1,1,0], actual)

if __name__ == '__main__':
    unittest.main()

