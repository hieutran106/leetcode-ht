import unittest
from .challenge_3 import solution

class MyTestCase(unittest.TestCase):
    def test_case_1(self):
        actual = solution(6, 1)
        self.assertEqual(actual, "8")

    def test_case_2(self):
        actual = solution(7, 3)
        self.assertEqual(actual, "13")

    def test_case_3(self):
        actual = solution(20, 4)
        self.assertEqual(actual, "6765")

    def test_case_4(self):
        actual = solution(100, 19)
        self.assertEqual(actual, "4224848179261915075")

    def test_case_5(self):
        actual = solution(10**5, 15)
        self.assertEqual(actual, "374653428746875")

    def test_case_6(self):
        actual = solution(2, 19)
        self.assertEqual(actual, "1")

    def test_case_7(self):
        actual = solution(10**6, 3)
        self.assertEqual(actual, "875")

    def test_case_8(self):
        actual = solution(2381, 13)
        self.assertEqual(actual, "0232565282581")



if __name__ == '__main__':
    unittest.main()
