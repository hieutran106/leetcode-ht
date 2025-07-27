import unittest
from typing import List

# Date: 2025-25-07

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        tmp = [(n,i) for i,n in enumerate(nums)]
        tmp.sort(reverse=True)
        tmp = tmp[:k]
        tmp.sort(key=lambda  x: x[1])
        ans = []
        for ele in tmp:
            ans.append(ele[0])
        return ans

    

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.maxSubsequence( nums = [2,1,3,3], k = 2)
        self.assertEqual(actual, [3, 3])
        
    def test_case_2(self):
        actual = self.s.maxSubsequence(nums = [-1,-2,3,4], k = 3)
        self.assertEqual(actual, [-1,3,4])

    def test_case_3(self):
        actual = self.s.maxSubsequence(nums = [3,4,3,3], k = 2)
        self.assertEqual([3,4], actual)

    def test_case_4(self):
        actual = self.s.maxSubsequence(nums = [-3,-2,3,4,-1], k = 3)
        self.assertEqual([3,4, -1], actual)

if __name__ == '__main__':
    unittest.main()

