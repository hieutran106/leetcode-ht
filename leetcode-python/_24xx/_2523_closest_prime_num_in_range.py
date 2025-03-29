import math
import unittest
from typing import List

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def get_primes(left, right):
            nums = [True] * (right + 1)
            nums[0] = False
            nums[1] = False
            for i in range(2, math.floor(math.sqrt(right)) + 1):
                if nums[i] is False:
                    continue
                for j in range(i+i, right + 1, i):
                    nums[j] = False
            ans = []
            for i in range(2, right + 1):
                if nums[i] is True and left <= i <= right:
                    ans.append(i)
            return ans
        nums = get_primes(left, right)
        if len(nums) <= 1:
            return [-1, -1]
        ans = [nums[0], nums[1]]
        d = nums[1] - nums[0]
        for i in range(len(nums) -1):
            if nums[i+1] - nums[i] < d:
                d = nums[i+1] - nums[i]
                ans = [nums[i], nums[i+1]]
        return ans

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.closestPrimes(left = 10, right = 19)
        self.assertEqual([11, 13], actual)
        
    def test_case_2(self):
        actual = self.s.closestPrimes(left = 4, right = 6)
        self.assertEqual([-1, -1], actual)

    def test_case_3(self):
        actual = self.s.closestPrimes(left = 2, right = 11)
        self.assertEqual([2, 3], actual)

    def test_case_3(self):
        actual = self.s.closestPrimes(left = 1, right = 1000000)
        self.assertEqual([2, 3], actual)

    def test_case_4(self):
        actual = self.s.closestPrimes(left = 1, right = 1)
        self.assertEqual([-1, -1], actual)

if __name__ == '__main__':
    unittest.main()

