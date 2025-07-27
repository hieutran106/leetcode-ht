import unittest
from typing import List

# Date: 2025-18-07
class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        min_val = min(target)
        print(f"Min val: {min_val=}")
        stack = [] # decreasing stack
        can_append = True
        for i, n in enumerate(target):
            val = n - min_val
            while stack and val >= stack[-1]:
                stack.pop()
            if val == 0:
                can_append = True
            if can_append:
                print(f"At {i=}, append {val=}, {n=}")
                stack.append(val)
                can_append = False

        print(stack)
        ans = 0
        return ans
    

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.minNumberOperations(target = [1,2,3,2,1])
        self.assertEqual(3, actual)
        
    def test_case_2(self):
        actual = self.s.minNumberOperations(target = [3,1,1,2])
        self.assertEqual(4, actual)

    def test_case_3(self):
        actual = self.s.minNumberOperations(target = [3,1,5,4,2])
        self.assertEqual(7, actual)

if __name__ == '__main__':
    unittest.main()

