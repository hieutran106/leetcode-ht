import unittest
from typing import List
import heapq
import collections
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def calculate_digit_sum(n: int):
            sum = 0
            while n > 0:
                sum += n % 10
                n = n // 10
            return sum
        d = collections.defaultdict(list) # dictionary (digit_sum, max heap of numbers that have the same digit sum)
        for n in nums:
            digit_sum = calculate_digit_sum(n)
            heapq.heappush(d[digit_sum], -n) # max heap
        ans = -1
        for digit_sum, nums in d.items():
            print(digit_sum, nums)
            if len(nums) >= 2:
                biggest = heapq.heappop(nums) # take out 2 biggest number
                second_biggest = heapq.heappop(nums)
                ans = max(ans, abs(biggest + second_biggest))
        return ans
class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.maximumSum(nums = [18,43,36,13,7])
        self.assertEqual(actual, 54)
        
    def test_case_2(self):
        actual = self.s.maximumSum(nums = [10,12,19,14])
        self.assertEqual(actual, -1)

    def test_case_3(self):
        actual = self.s.maximumSum(nums = [10])
        self.assertEqual(actual, -1)

    def test_case_4(self):
        actual = self.s.maximumSum(nums = [229,398,269,317,420,464,491,218,439,153,482,169,411,93,147,50,347,210,251,366,401])
        self.assertEqual(actual, 973)

    def test_case_5(self):
        actual = self.s.maximumSum(nums = [279,169,463,252,94,455,423,315,288,64,494,337,409,283,283,477,248,8,89,166,188,186,128])
        self.assertEqual(actual, 872)
if __name__ == '__main__':
    unittest.main()

