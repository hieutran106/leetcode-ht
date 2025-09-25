import unittest
from typing import List
import math
# Date: 2025-17-09
# Problem: 2197 replace_non_coprime_numbers
def calGCD(a, b):
    while b:
        a, b = b, a % b
    return a

class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack = []
        for n in nums:
            curr = n
            while stack and math.gcd(curr, stack[-1]) > 1:
                curr = math.lcm(curr, stack.pop())
            stack.append(curr)

        return stack

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.replaceNonCoprimes(nums = [6,4,3,2,7,6,2])
        self.assertEqual(actual, [12,7,6])

    def test_case_2(self):
        actual = self.s.replaceNonCoprimes([2,2,1,1,3,3,3])
        self.assertEqual(actual, [2,1,1,3])

    def test_case_3(self):
        actual = self.s.replaceNonCoprimes([4, 6, 12])
        self.assertEqual(actual, [12])

    def test_case_4(self):
        actual = self.s.replaceNonCoprimes([287,41,49,287,899,23,23,20677,5,825])
        self.assertEqual(actual, [2009,20677,825])

if __name__ == '__main__':
    unittest.main()

