import unittest
from typing import List

# Date: 2025-11-17
# Problem: 1437 check_all_one_k_places_away
class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        last_one = None
        for i, n in enumerate(nums):
            if n == 0:
                continue
            if last_one is None:
                last_one = i
                continue
            gap = i - last_one - 1
            if gap < k:
                return False
            last_one = i
        return True
    

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.kLengthApart(nums = [1,0,0,0,1,0,0,1], k = 2)
        self.assertEqual(True, actual)
        
    def test_case_2(self):
        actual = self.s.kLengthApart(nums = [1,0,0,1,0,1], k = 2)
        self.assertEqual(False, actual)

    def test_case_3(self):
        actual = self.s.kLengthApart(nums = [1], k = 0)
        self.assertEqual(True, actual)

    def test_case_4(self):
        actual = self.s.kLengthApart(nums = [0], k = 0)
        self.assertEqual(True, actual)

    def test_case_5(self):
        actual = self.s.kLengthApart(nums = [1,0,0,0], k = 1)
        self.assertEqual(True, actual)

    def test_case_6(self):
        actual = self.s.kLengthApart(nums = [1,0,0,0,1,0,0,1,0], k = 2)
        self.assertEqual(True, actual)

    def test_case_7(self):
        actual = self.s.kLengthApart(nums = [0, 0, 0, 1, 0, 0, 1, 0], k = 2)
        self.assertEqual(True, actual)

if __name__ == '__main__':
    unittest.main()

