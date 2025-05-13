import unittest
from typing import List

#2025-06-04
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        all_subsets = []
        path = []

        def backtrack(i):
            if i == len(nums):
                return
            ans = 0
            for j in range(i, len(nums)):
                path.append(nums[j])
                all_subsets.append(path.copy())
                backtrack(j + 1)
                path.pop()
            return ans
        backtrack(0)
        print(all_subsets)
        ans = 0
        for subset in all_subsets:
            xor_value = 0
            for n in subset:
                xor_value = xor_value ^ n
            ans+= xor_value
        return ans
class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.subsetXORSum(nums = [1,3])
        self.assertEqual(6, actual)
        
    def test_case_2(self):
        actual = self.s.subsetXORSum(nums = [5,1,6])
        self.assertEqual(28, actual)

    def test_case_3(self):
        actual = self.s.subsetXORSum(nums = [3,4,5,6,7,8])
        self.assertEqual(480, actual)

    def test_case_4(self):
        actual = self.s.subsetXORSum(nums = [3])
        self.assertEqual(3, actual)

if __name__ == '__main__':
    unittest.main()

