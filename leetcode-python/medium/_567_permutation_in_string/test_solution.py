import unittest
from .solution import Solution, Solution2

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution2()

    def test_case1(self):
        actual = self.s.checkInclusion("ab", "eidbaooo")
        self.assertEqual(actual, True)

    def test_case2(self):
        actual = self.s.checkInclusion("ab", "eidboaoo")
        self.assertEqual(actual, False)

    def test_case3(self):
        actual = self.s.checkInclusion("ab", "ba")
        self.assertEqual(actual, True)

    def test_case4(self):
        actual = self.s.checkInclusion("a", "c")
        self.assertEqual(actual, False)

    def test_case5(self):
        actual = self.s.checkInclusion("ab", "c")
        self.assertEqual(actual, False)

    def test_case6(self):
        actual = self.s.checkInclusion("abc", "ababababababbbbbacbad")
        self.assertEqual(actual, True)

if __name__ == '__main__':
    unittest.main()

