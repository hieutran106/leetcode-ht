import unittest
from .solution import Solution

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case1(self):
        s = "leetcode"
        word_dict = ["leet", "code"]
        actual = self.s.wordBreak(s, word_dict)
        self.assertEqual(True, actual)

    def test_case2(self):
        s = "catsandog"
        word_dict = ["cats", "dog", "sand", "and", "cat"]
        actual = self.s.wordBreak(s, word_dict)
        self.assertEqual(False, actual)

    def test_case3(self):
        s = "applepenapple"
        word_dict = ["apple", "pen"]
        actual = self.s.wordBreak(s, word_dict)
        self.assertEqual(True, actual)

    def test_case4(self):
        s = "applepenapple"
        word_dict = ["apple", "penapple"]
        actual = self.s.wordBreak(s, word_dict)
        self.assertEqual(True, actual)

    def test_case5(self):
        s = "abcabcabcded"
        word_dict = ["a", "b", "c", "d"]
        actual = self.s.wordBreak(s, word_dict)
        self.assertEqual(False, actual)


if __name__ == '__main__':
    unittest.main()

