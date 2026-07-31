import unittest
from typing import List

# Date: 2026-07-29
# Problem: 3517 smallest_palindromic_rearrangement
class Solution:
    def smallestPalindrome(self, s: str) -> str:
        counter = [0] * 26
        for c in s:
            counter[ord(c) - ord('a')] += 1

        n = len(s)
        ans = ["_" for _ in range(n)]
        mid = len(ans) // 2


        j = 0
        for i in range(26):
            char = chr(i + ord('a'))
            f = counter[i]
            if f == 0:
                continue
            if f % 2 == 1:
                ans[mid] = char
                f = f - 1
            for k in range(f//2):
                ans[j+k] = char
                ans[n-1 -j -k] = char
            j += f//2


        ans = "".join(ans)
        return ans
    

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.smallestPalindrome(s = "z")
        self.assertEqual(actual, "z")
        
    def test_case_2(self):
        actual = self.s.smallestPalindrome(s="babab")
        self.assertEqual(actual, "abbba")

    def test_case_3(self):
        actual = self.s.smallestPalindrome(s="daccad")
        self.assertEqual(actual, "acddca")

    def test_case_4(self):
        actual = self.s.smallestPalindrome(s="cbababc")
        self.assertEqual(actual, "abcbcba")

if __name__ == '__main__':
    unittest.main()

