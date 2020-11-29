import unittest
from .solution import Solution

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case1(self):
        actual = self.s.findTheDifference("abcd", "abcde")
        self.assertEqual(actual, "e")

    def test_case2(self):
        actual = self.s.findTheDifference("", "y")
        self.assertEqual(actual, "y")

    def test_case3(self):
        actual = self.s.findTheDifference("abcd", "abzcd")
        self.assertEqual(actual, "z")

    def test_case4(self):
        actual = self.s.findTheDifference("aaabbbccc", "abceabccba")
        self.assertEqual(actual, "e")

    def test_case5(self):
        actual = self.s.findTheDifference("a", "aa")
        self.assertEqual(actual, "a")

if __name__ == '__main__':
    unittest.main()

