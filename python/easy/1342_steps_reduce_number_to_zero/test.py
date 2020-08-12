import unittest
from .solution import Solution
from .solution2 import Solution2

class TestSum(unittest.TestCase):
    def getSolution():
        return Solution2()

    def test_case_1(self):
        s = TestSum.getSolution()
        actual = s.numberOfSteps(14)
        print(actual)
        self.assertEqual(actual, 6)

    def test_case_2(self):
        s = TestSum.getSolution()
        actual = s.numberOfSteps(8)
        self.assertEqual(actual, 4)

    def test_case_3(self):
        s = TestSum.getSolution()
        actual = s.numberOfSteps(123)
        self.assertEqual(actual, 12)

    def test_case_4(self):
        s = TestSum.getSolution()
        actual = s.numberOfSteps(0)
        self.assertEqual(actual, 0)


if __name__ == '__main__':
    unittest.main()