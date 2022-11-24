import unittest
from .solution import Solution

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        actual = self.s.isPalindrome("A man, a plan, a canal: Panama")
        self.assertEqual(True, actual)

    def test_case_2(self):
        actual = self.s.isPalindrome("race a car")
        self.assertEqual(False, actual)

    def test_case_3(self):
        actual = self.s.isPalindrome(" ")
        self.assertEqual(True, actual)

    def test_case_4(self):
        actual = self.s.isPalindrome(".a")
        self.assertEqual(True, actual)

    def test_case_5(self):
        actual = self.s.isPalindrome("0P")
        self.assertEqual(False, actual)

    def test_case_6(self):
        actual = self.s.isPalindrome("ab.a")
        self.assertEqual(True, actual)

    def test_case_7(self):
        actual = self.s.isPalindrome("a.a")
        self.assertEqual(True, actual)

    def test_case_8(self):
        actual = self.s.isPalindrome("1b1")
        self.assertEqual(True, actual)

if __name__ == '__main__':
    unittest.main()

