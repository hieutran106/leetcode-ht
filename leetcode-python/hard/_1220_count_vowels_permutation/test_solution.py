import unittest
from .solution import Solution

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    def test_case_1(self):
        actual = self.s.countVowelPermutation(1)
        self.assertEqual(5, actual)

    def test_case_2(self):
        actual = self.s.countVowelPermutation(2)
        self.assertEqual(10, actual)

    def test_case_3(self):
        actual = self.s.countVowelPermutation(5)
        self.assertEqual(68, actual)

if __name__ == '__main__':
    unittest.main()

