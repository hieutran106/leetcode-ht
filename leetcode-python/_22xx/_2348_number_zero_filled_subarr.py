import unittest
from typing import List

# Date: 2025-19-08
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        l = 0
        ans = 0
        for r, curr in enumerate(nums):
            if curr == 0 and (r == len(nums) -1 or nums[r+1] !=0):
                while nums[l] != 0:
                    l += 1
                w = r - l + 1
                print(f"Zero sub array {l=}, {r=}, {w=}")
                ans += w * (w+1)//2
                l = r + 1

        return ans
    

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.zeroFilledSubarray(nums = [1,3,0,0,2,0,0,4])
        self.assertEqual(6, actual)
        
    def test_case_2(self):
        actual = self.s.zeroFilledSubarray(nums = [0,0,0,2,0,0])
        self.assertEqual(9, actual)

    def test_case_3(self):
        actual = self.s.zeroFilledSubarray(nums = [2,10,2019])
        self.assertEqual(0, actual)

    def test_case_4(self):
        actual = self.s.zeroFilledSubarray(nums = [1, 2, 3, 4, 0, 0, 0, 0, 1, 0])
        self.assertEqual(11, actual)

if __name__ == '__main__':
    unittest.main()

