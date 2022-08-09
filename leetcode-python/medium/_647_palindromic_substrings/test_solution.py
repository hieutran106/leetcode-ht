import unittest
from .solution import Solution

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case1(self):
        actual = self.s.countSubstrings("abc")
        self.assertEqual(actual, 3)

    def test_case2(self):
        actual = self.s.countSubstrings("aaa")
        self.assertEqual(actual, 6)

    def test_case4(self):
        actual = self.s.countSubstrings("aabaad")
        self.assertEqual(actual, 10)

    def test_case5(self):
        actual = self.s.countSubstrings("baabb")
        self.assertEqual(actual, 8)

if __name__ == '__main__':
    unittest.main()

