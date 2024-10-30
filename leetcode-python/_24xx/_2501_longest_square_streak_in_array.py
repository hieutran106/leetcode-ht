import unittest
from typing import List

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        count = {}
        for n in nums:
            if n not in count:
                count[n*n] = 1
            else:

                count[n*n] = count[n] + 1
                del count[n]
        print(count)
        ans = max(count.values())
        if ans == 1:
            return -1
        return ans
class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.longestSquareStreak(nums = [4,3,6,16,8,2])
        self.assertEqual(actual, 3)
        
    def test_case_2(self):
        actual = self.s.longestSquareStreak([2,3,5,6,7])
        self.assertEqual(actual, -1)

    def test_case_3(self):
        actual = self.s.longestSquareStreak([3, 9, 81, 2, 4, 16, 256])
        self.assertEqual(actual, 4)

    def test_case_4(self):
        actual = self.s.longestSquareStreak([2,4,4,2])
        self.assertEqual(actual, 2)
    def test_case_5(self):
        actual = self.s.longestSquareStreak([4, 2])
        self.assertEqual(actual, 2)

if __name__ == '__main__':
    unittest.main()

