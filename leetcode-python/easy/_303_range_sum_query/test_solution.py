import unittest
from .solution import NumArray


class MyTestCase(unittest.TestCase):

    def test_case_1(self):
        num_array = NumArray([-2, 0, 3, -5, 2, -1])
        self.assertEqual(1, num_array.sumRange(0, 2))
        self.assertEqual(-1, num_array.sumRange(2, 5))
        self.assertEqual(-3, num_array.sumRange(0, 5))


if __name__ == '__main__':
    unittest.main()
