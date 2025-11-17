import unittest
from typing import List

# Date: 2025-11-17
# Problem: 1513 number_substr_with_only_one
class Solution:
    def numSub(self, s: str) -> int:
        ans = 0
        one_count = 0
        MOD = 10 ** 9 + 1
        for i,c  in enumerate(s):
            if c == '1':
                one_count += 1
                if i == len(s) - 1 or s[i+1] == '0':
                    ans += (one_count * (one_count + 1) // 2) % MOD
                    one_count = 0

        return ans
    

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.numSub(s = "0110111")
        self.assertEqual(9, actual)
        
    def test_case_2(self):
        actual = self.s.numSub(s = "101")
        self.assertEqual(2, actual)

    def test_case_3(self):
        actual = self.s.numSub(s = "111111")
        self.assertEqual(21, actual)

    def test_case_3(self):
        actual = self.s.numSub(s = "0")
        self.assertEqual(0, actual)

if __name__ == '__main__':
    unittest.main()

