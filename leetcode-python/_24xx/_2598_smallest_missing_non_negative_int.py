import collections
import unittest
from typing import List

# Date: 2025-10-17
# Problem: 2598 smallest_missing_non_negative_int
class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        counter = collections.defaultdict(int)
        for n in nums:
            counter[n % value] += 1
        for i in range(10**5 + 1):
            r = i % value
            if r in counter:
                counter[r] -= 1
                if counter[r] == 0:
                    del counter[r]
            else:
                return i
        return -1

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.findSmallestInteger(nums = [1,-10,7,13,6,8], value = 5)
        self.assertEqual(actual, 4)
        
    def test_case_2(self):
        actual = self.s.findSmallestInteger(nums = [1,-10,7,13,6,8], value = 7)
        self.assertEqual(actual, 2)

    def test_case_3(self):
        actual = self.s.findSmallestInteger(nums = [0, 1, 2, 3], value = 3)
        self.assertEqual(actual, 4)

    def test_case_4(self):
        actual = self.s.findSmallestInteger(nums = [3,0,3,2,4,2,1,1,0,4], value = 5)
        self.assertEqual(actual, 10)

    def test_case_5(self):
        actual = self.s.findSmallestInteger(nums = [0, 0, 0, 0, 0, 0], value = 1)
        self.assertEqual(actual, 6)

if __name__ == '__main__':
    unittest.main()

