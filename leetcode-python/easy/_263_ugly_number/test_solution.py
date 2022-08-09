import unittest
from .solution import Solution

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()    

    def test_case1(self):
        actual = self.s.isUgly(6)
        self.assertEqual(actual, True)

    def test_case2(self):
        actual = self.s.isUgly(8)
        self.assertEqual(actual, True)

    def test_case3(self):
        actual = self.s.isUgly(14)
        self.assertEqual(actual, False)

    def test_case4(self):
        actual = self.s.isUgly(1)
        self.assertEqual(actual, True)

        actual = self.s.isUgly(22)
        self.assertEqual(actual, False)

        actual = self.s.isUgly(23)
        self.assertEqual(actual, False)



if __name__ == '__main__':
    unittest.main()

