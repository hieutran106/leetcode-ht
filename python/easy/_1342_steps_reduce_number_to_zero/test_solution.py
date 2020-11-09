import unittest
from easy._1342_steps_reduce_number_to_zero.solution2 import Solution2

class TestSolution(unittest.TestCase):

    @classmethod
    def getSolution(cls):
        return Solution2()

    def test_case_1(self):
        s = TestSolution.getSolution()
        actual = s.numberOfSteps(14)
        print(actual)
        self.assertEqual(actual, 6)

    def test_case_2(self):
        s = TestSolution.getSolution()
        actual = s.numberOfSteps(8)
        self.assertEqual(actual, 4)

    def test_case_3(self):
        s = TestSolution.getSolution()
        actual = s.numberOfSteps(123)
        self.assertEqual(actual, 12)

    def test_case_4(self):
        s = TestSolution.getSolution()
        actual = s.numberOfSteps(0)
        self.assertEqual(actual, 0)


if __name__ == '__main__':
    unittest.main()