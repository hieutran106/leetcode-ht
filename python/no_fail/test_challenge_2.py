import unittest
from .challenge_2 import solution

class MyTestCase(unittest.TestCase):
    def test_case_1(self):
        actual = solution("2020-01-01")
        self.assertEqual(actual, 59)




if __name__ == '__main__':
    unittest.main()
