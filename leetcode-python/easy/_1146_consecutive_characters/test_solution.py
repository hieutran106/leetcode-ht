import unittest
from .solution import Solution

class MyTestCase(unittest.TestCase):
    def test_case_1(self):
        s = Solution()
        actual = s.maxPower("tourist")
        self.assertEqual(actual, 1)

    def test_case_2(self):
        s = Solution()
        actual = s.maxPower("abbcccddddeeeeedcba")
        self.assertEqual(actual, 5)

    def test_case_3(self):
        s = Solution()
        actual = s.maxPower("triplepillooooow")
        self.assertEqual(actual, 5)

    def test_case_4(self):
        s = Solution()
        actual = s.maxPower("leetcode")
        self.assertEqual(actual, 2)

    def test_case_5(self):
        s = Solution()
        actual = s.maxPower("ccbccbb")
        self.assertEqual(actual, 2)

    def test_case_6(self):
        s = Solution()
        actual = s.maxPower("ccbcccbb")
        self.assertEqual(actual, 3)

    def test_case_7(self):
        s = Solution()
        actual = s.maxPower("cc")
        self.assertEqual(actual, 2)

    def test_case_8(self):
        s = Solution()
        actual = s.maxPower("aabbbbbccccdddddddeffffffggghhhhhiiiiijjjkkkkkllllmmmmmnnnnnoopppqrrrrsssttttuuuuvvvvwwwwwwwxxxxxyyyzzzzzzzz")
        self.assertEqual(actual, 8)

    def test_case_9(self):
        s = Solution()
        actual = s.maxPower("cccbbc")
        self.assertEqual(actual, 3)

    def test_case_10(self):
        s = Solution()
        actual = s.maxPower("cccbbbcccc")
        self.assertEqual(actual, 4)

if __name__ == '__main__':
    unittest.main()
