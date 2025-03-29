import unittest
from typing import List

#2025-13-03
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        return 0

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.numberOfSubarrays(nums = [1,1,2,1,1], k = 3)
        self.assertEqual(2, actual)
        
    def test_case_2(self):
        actual = self.s.numberOfSubarrays(nums = [2,4,6], k = 1)
        self.assertEqual(0, actual)

    def test_case_3(self):
        actual = self.s.numberOfSubarrays(nums = [2,2,2,1,2,2,1,2,2,2], k = 2)
        self.assertEqual(16, actual)

if __name__ == '__main__':
    unittest.main()

