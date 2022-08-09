import unittest
from .solution import Solution

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        actual = self.s.characterReplacement("ABAB", 2)
        self.assertEqual(actual, 4)

    def test_case_2(self):
        actual = self.s.characterReplacement("AABABBA", 1)
        self.assertEqual(actual, 4)

    def test_case_3(self):
        actual = self.s.characterReplacement("ABCAAAAC", 0)
        self.assertEqual(actual, 4)

    def test_case_4(self):
        actual = self.s.characterReplacement("A", 0)
        self.assertEqual(actual, 1)

    def test_case_5(self):
        actual = self.s.characterReplacement("A", 1)
        self.assertEqual(actual, 1)

    def test_case_6(self):
        actual = self.s.characterReplacement("A", 2)
        self.assertEqual(actual, 1)

    def test_case_7(self):
        actual = self.s.characterReplacement("AAAAABB", 2)
        self.assertEqual(actual, 7)

    def test_case_8(self):
        actual = self.s.characterReplacement("ABBB", 2)
        self.assertEqual(actual , 4)

    def test_case_9(self):
        actual = self.s.characterReplacement("AABBBB", 2)
        self.assertEqual(actual , 6)

    def test_case_10(self):
        actual = self.s.characterReplacement("BAAAB", 2)
        self.assertEqual(actual, 5)

if __name__ == '__main__':
    unittest.main()

