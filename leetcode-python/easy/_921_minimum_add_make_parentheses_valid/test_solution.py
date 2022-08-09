import unittest
from easy._921_minimum_add_make_parentheses_valid.solution import Solution


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        s = Solution()
        actual = s.minAddToMakeValid("())")
        self.assertEqual(actual, 1)

    def test_case_2(self):
        s = Solution()
        actual = s.minAddToMakeValid("(((")
        self.assertEqual(actual, 3)

    def test_case_3(self):
        s = Solution()
        actual = s.minAddToMakeValid("()")
        self.assertEqual(actual, 0)

    def test_case_4(self):
        s = Solution()
        actual = s.minAddToMakeValid("()))((")
        self.assertEqual(actual, 4)

    def test_case_5(self):
        s = Solution()
        actual = s.minAddToMakeValid("())(")
        self.assertEqual(actual, 2)

    def test_case_6(self):
        s = Solution()
        actual = s.minAddToMakeValid("")
        self.assertEqual(actual, 0)

if __name__ == '__main__':
    unittest.main()
