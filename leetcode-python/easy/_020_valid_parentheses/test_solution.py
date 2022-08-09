import unittest
from .solution import Solution

class MyTestCase(unittest.TestCase):
    def test_case1(self):
        s = Solution()
        actual = s.isValid("{[]}")
        self.assertEqual(actual, True)

    def test_case2(self):
        s = Solution()
        actual = s.isValid("([)]")
        self.assertEqual(actual, False)

    def test_case3(self):
        s = Solution()
        actual = s.isValid("()[]{}")
        self.assertEqual(actual, True)

    def test_case4(self):
        s = Solution()
        actual = s.isValid("[")
        self.assertEqual(actual, False)

if __name__ == '__main__':
    unittest.main()
