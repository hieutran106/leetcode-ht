import unittest
from typing import List

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        # put all prefix in a set
        prefixes = set()
        for num in arr1:
            while num > 0:
                prefixes.add(num)
                num = num // 10
        print(prefixes)
        ans = 0
        for num in arr2:
            while num > 0:
                if num in prefixes:
                    ans = max(ans, len(str(num)))
                    break
                num = num //10

        return ans
class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.longestCommonPrefix(arr1 = [1,10,100], arr2 = [1000])
        self.assertEqual(3, actual)
        
    def test_case_2(self):
        actual = self.s.longestCommonPrefix(arr1 = [1,2,3], arr2 = [4,4,4])
        self.assertEqual(0, actual)

    def test_case_4(self):
        actual = self.s.longestCommonPrefix(arr1 = [1,2,3, 1234567], arr2 = [4,4,4, 123456, 1234, 5678])
        self.assertEqual(6, actual)

    def test_case_4(self):
        actual = self.s.longestCommonPrefix(arr1 = [4,4,4, 123456, 1234, 5678], arr2 = [1,2,3, 1234567])
        self.assertEqual(6, actual)

if __name__ == '__main__':
    unittest.main()

