import unittest
import collections

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        set1 = set(word1)
        set2 = set(word2)
        if set1 != set2:
            return False

        freq1 = [0] * 26
        freq2 = [0] * 26
        for c in word1:
            index = ord(c) - ord('a')
            freq1[index] += 1

        for c in word2:
            index = ord(c) - ord('a')
            freq2[index] += 1

        freq1.sort()
        freq2.sort()
        return freq1 == freq2


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.closeStrings(word1 = "abc", word2 = "bca")
        self.assertEqual(True, actual)
        
    def test_case_2(self):
        actual = self.s.closeStrings(word1 = "a", word2 = "aa")
        self.assertEqual(False, actual)

    def test_case_3(self):
        actual = self.s.closeStrings(word1 = "cabbba", word2 = "abbccc")
        self.assertEqual(True, actual)

    def test_case_4(self):
        actual = self.s.closeStrings(word1 = "a", word2 = "b")
        self.assertEqual(False, actual)

    def test_case_5(self):
        actual = self.s.closeStrings(word1 = "uau", word2 = "ssx")
        self.assertEqual(False, actual)

if __name__ == '__main__':
    unittest.main()

