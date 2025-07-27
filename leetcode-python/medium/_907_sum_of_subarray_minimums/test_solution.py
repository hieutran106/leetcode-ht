import unittest
from .solution import Solution, Solution2
from os.path import abspath, join

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution2()

    def test_case1(self):
        actual = self.s.sumSubarrayMins([3, 1, 2, 4])
        self.assertEqual(17, actual)

    def test_case2(self):
        actual = self.s.sumSubarrayMins([1, 2])
        self.assertEqual(4, actual)

    def test_case3(self):
        actual = self.s.sumSubarrayMins([1])
        self.assertEqual(1, actual)

    def test_case4(self):
        actual = self.s.sumSubarrayMins([3, 2, 2, 3])
        self.assertEqual(22, actual)

    def test_case5(self):
        actual = self.s.sumSubarrayMins([71,55,82,55])
        self.assertEqual(593, actual)

    def test_case_7(self):
        actual = self.s.sumSubarrayMins([3, 7, 8, 4])
        self.assertEqual(46, actual)

    def test_case6(self):
        file_path = join('_907_sum_of_subarray_minimums', 'input.txt')
        with open(file_path, 'r') as reader:
            text = reader.read().strip()
            numberStrs = text.split(" ")
            input = list(map(lambda x: int(x), numberStrs))
            actual = self.s.sumSubarrayMins(input)
            self.assertEqual(667452382, actual)



if __name__ == '__main__':
    unittest.main()

