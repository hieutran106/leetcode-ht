import unittest
from .solution import Solution

class MyTestCase(unittest.TestCase):
    def test_case_1(self):
        s = Solution()
        input = ["h","e","l","l","o"]
        s.reverseString(input)
        self.assertEqual(input, ["o","l","l","e","h"])

    def test_case_2(self):
        s = Solution()
        input = ["H","a","n","n","a","h"]
        s.reverseString(input)
        self.assertEqual(input, ["h","a","n","n","a","H"])

    def test_case_3(self):
        s = Solution()
        input = []
        s.reverseString(input)
        self.assertEqual(input, [])

    def test_case_4(self):
        s = Solution()
        input = ["a"]
        s.reverseString(input)
        self.assertEqual(input, ["a"])

    def test_case_5(self):
        s = Solution()
        input = ["h","e","l","l","o"]
        s.reverseString(input)
        self.assertEqual(input, ["o","l","l","e","h"])
if __name__ == '__main__':
    unittest.main()
