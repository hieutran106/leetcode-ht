import unittest
from typing import List
import collections


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # Iterate from right to left and keep track of seen
        # If we see a nums[i], we remove 0..i
        seen = set()
        for i in range(len(nums) -1, -1, -1):
            if nums[i] in seen:
                return i//3 + 1
            seen.add(nums[i])
        return 0
#2025-08-04
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        ans = 0
        def is_distinct(d):
            for v in d.values():
                if v > 1:
                    return False
            return True

        for i in range(0, len(nums)):
            if i %3 == 0:

                if is_distinct(counter):
                    return ans
                else:
                    ans += 1
            counter[nums[i]] -= 1
        return ans

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.minimumOperations(nums = [1,2,3,4,2,3,3,5,7])
        self.assertEqual(2, actual)
        
    def test_case_2(self):
        actual = self.s.minimumOperations(nums = [4,5,6,4,4])
        self.assertEqual(2, actual)

    def test_case_3(self):
        actual = self.s.minimumOperations(nums = [6,7,8,9])
        self.assertEqual(0, actual)

    def test_case_4(self):
        actual = self.s.minimumOperations(nums = [1,2,3,4,1])
        self.assertEqual(1, actual)

if __name__ == '__main__':
    unittest.main()

