import unittest
from .challenge_1 import solution

class MyTestCase(unittest.TestCase):
    def test_case_1(self):
        actual = solution("2020-01-01")
        self.assertEqual(actual, 59)

    def test_case_2(self):
        actual = solution("2020-02-29")
        self.assertEqual(actual, 0)

    def test_case_3(self):
        actual = solution("0004-02-29")
        self.assertEqual(actual, 0)

    def test_case_4(self):
        actual = solution("0004-02-28")
        self.assertEqual(actual, 1)

    def test_case_5(self):
        actual = solution("0004-03-01")
        self.assertEqual(actual, 1460)

    def test_case_6(self):
        actual = solution("abcd-03-01")
        self.assertEqual(actual, -1)


if __name__ == '__main__':
    unittest.main()
