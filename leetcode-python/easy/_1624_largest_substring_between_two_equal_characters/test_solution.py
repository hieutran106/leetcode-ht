import unittest
from .solution import Solution


class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        memo = {s[0]: 0}
        distance = -1
        for i in range(1, len(s)):
            c= s[i]
            if c in memo:
                distance = max(distance, i - memo[c] - 1)
            else:
                memo[c] = i
        return distance

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.maxLengthBetweenEqualCharacters(s = "aa")
        self.assertEqual(actual, 0)
        
    def test_case_2(self):
        actual = self.s.maxLengthBetweenEqualCharacters(s="abca")
        self.assertEqual(actual, 2)

    def test_case_3(self):
        actual = self.s.maxLengthBetweenEqualCharacters(s = "cbzxy")
        self.assertEqual(actual, -1)

    def test_case_4(self):
        actual = self.s.maxLengthBetweenEqualCharacters(s = "aaaa")
        self.assertEqual(actual, 2)

    def test_case_5(self):
        actual = self.s.maxLengthBetweenEqualCharacters(s = "aaaabbbbbbb")
        self.assertEqual(actual, 5)

if __name__ == '__main__':
    unittest.main()

