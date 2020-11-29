import unittest
from .solution import Solution, Solution2

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution2()

    def test_case1(self):
        actual = self.s.isAnagram("anagram", "nagaram")
        self.assertEqual(True, actual)

    def test_case2(self):
        actual = self.s.isAnagram("rat", "car")
        self.assertEqual(False, actual)

    def test_case4(self):
        actual = self.s.isAnagram("test", "")
        self.assertEqual(False, actual)

    def test_case5(self):
        actual = self.s.isAnagram("", "test")
        self.assertEqual(False, actual)

    def test_case6(self):
        actual = self.s.isAnagram("", "")
        self.assertEqual(True, actual)

if __name__ == '__main__':
    unittest.main()

