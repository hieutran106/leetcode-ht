import unittest
from typing import List

# Date: 2025-27-07
class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        tmp = [nums[0]]
        for n in nums[1:]:
            if n == tmp[-1]:
                continue
            tmp.append(n)

        ans = 0
        for i in range(1, len(tmp) - 1):
            if tmp[i-1] < tmp[i] and tmp[i+1] < tmp[i]:
                ans += 1
            if tmp[i-1] > tmp[i] and tmp[i+1] > tmp[i]:
                ans += 1


        return ans

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.countHillValley(nums = [2,4,1,1,6,5])
        self.assertEqual(3, actual)
        
    def test_case_2(self):
        actual = self.s.countHillValley(nums = [6,6,5,5,4,1])
        self.assertEqual(0, actual)

    def test_case_3(self):
        actual = self.s.countHillValley(nums = [6, 6, 5, 4, 4, 7, 7, 6])
        self.assertEqual(2, actual)

if __name__ == '__main__':
    unittest.main()

