import unittest
from .solution import Solution

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        actual = self.s.reorderedPowerOf2(1)
        self.assertEqual(actual, True)

    def test_case_2(self):
        actual = self.s.reorderedPowerOf2(10)
        self.assertEqual(actual, False)

    def test_case_3(self):
        actual = self.s.reorderedPowerOf2(2104)
        self.assertEqual(actual, True)

    def test_case_4(self):
        actual = self.s.reorderedPowerOf2(125)
        self.assertEqual(actual, True)

    def test_case_5(self):
        actual = self.s.reorderedPowerOf2(126)
        self.assertEqual(actual, False)

if __name__ == '__main__':
    unittest.main()

