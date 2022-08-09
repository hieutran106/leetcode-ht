import unittest
from .solution import Solution

class MyTestCase(unittest.TestCase):
    def test_case_1(self):
        s = Solution()
        actual = s.countVowelStrings(1)
        self.assertEqual(actual, 5)

    def test_case_2(self):
        s = Solution()
        actual = s.countVowelStrings(2)
        self.assertEqual(actual, 15)

    def test_case_3(self):
        s = Solution()
        actual = s.countVowelStrings(33)
        self.assertEqual(actual, 66045)


if __name__ == '__main__':
    unittest.main()
