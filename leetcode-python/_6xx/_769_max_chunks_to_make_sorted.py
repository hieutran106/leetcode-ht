import unittest
from typing import List

# Date: 2025-12-06
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        desired = set()
        actual = set()
        ans = 0
        for i,v in enumerate(arr):
            desired.add(i)
            actual.add(v)
            if desired == actual:
                ans += 1
                desired.clear()
                actual.clear()

        return ans
class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.maxChunksToSorted(arr = [4,3,2,1,0])
        self.assertEqual(1, actual)
        
    def test_case_2(self):
        actual = self.s.maxChunksToSorted(arr = [1,0,2,3,4])
        self.assertEqual(4, actual)

    def test_case_3(self):
        actual = self.s.maxChunksToSorted(arr = [1,0,3,5,2,4,6,7,8,10,9])
        self.assertEqual(6, actual)

if __name__ == '__main__':
    unittest.main()

