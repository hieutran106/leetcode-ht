import unittest
from typing import List
import collections


# Date: 2025-26-05
class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        freq = collections.defaultdict(int)
        for w in words:
            freq[w] += 1

        print(freq)
        ans = 0
        at_root = 0
        for w, count in freq.items():
            if w[0] != w[1]:
                palin_word = w[1] + w[0]
                if palin_word in freq:
                    ans += min(freq[w], freq[palin_word]) * 2
            else:
                if freq[w] % 2 == 0:
                    ans += freq[w] * 2
                else:
                    if freq[w] > at_root:
                        if at_root > 0:
                            ans -= 2
                        ans += freq[w] * 2
                        at_root = freq[w]
                    else:
                        ans += (freq[w] - 1) * 2

        return ans


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        actual = self.s.longestPalindrome(words=["lc", "cl", "gg"])
        self.assertEqual(6, actual)

    def test_case_2(self):
        actual = self.s.longestPalindrome(words=["ab", "ty", "yt", "lc", "cl", "ab"])
        self.assertEqual(8, actual)

    def test_case_3(self):
        actual = self.s.longestPalindrome(words=["cc", "ll", "xx"])
        self.assertEqual(2, actual)

    def test_case_4(self):
        actual = self.s.longestPalindrome(words=["cc", "cc", "cc", "aa", "bb", "bb"])
        self.assertEqual(10, actual)

    def test_case_5(self):
        actual = self.s.longestPalindrome(words=["nt","tt","yt","yn","yy","yn","nt","yn","nt","yy","ny","yn","ny","nn","nn","yy","nn","yt","yn","tn","yy","yn","nt","tt","yn","ny","nn","yn","nn","nt","ny","ty","ny","nt","ny","tn","nt","yy","nn","yy","nn","yt","yy","yn","nn","ny","ty","nn","nt","nt","ny","yy","tn","yy","tn","ty","ny","nt","ty","yt","yn","nn","ny","yt","nt","tt","nt","yy","yt","nt","tt","yn","tn","tn","nt","yt","yn","ty","yy","ty","tn","tn","yn","ty","ty","tn","nn","nt","nn","nn","tt","yy","ty","ny","yy","ny"])
        self.assertEqual(170, actual)

    def test_case_6(self):
        words = ["tt"] *5 + ['yy']*13 +['nn']*13
        actual = self.s.longestPalindrome(words)
        self.assertEqual(58, actual)

if __name__ == '__main__':
    unittest.main()
