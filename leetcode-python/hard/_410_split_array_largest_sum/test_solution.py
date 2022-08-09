import unittest
from .solution import Solution

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_is_feasible1(self):
        nums = [1, 6, 4, 1, 2]
        m = 3
        expects = {5: False, 6: False, 7: True, 8:True, 9: True, 10:True}
        for i in range(5, 11):
            with self.subTest(f"Testing nums={nums}, m={m}, largest_sum={i}"):
                actual = self.s.is_feasible(nums, m, i)
                self.assertEqual(actual, expects[i])

    def test_is_feasible2(self):
        nums = [1, 4, 4]
        m = 3
        expects = {1: False, 2: False, 3: False, 4: True}
        for i in range(1, 5):
            with self.subTest(f"Testing nums={nums}, m={m}, largest_sum={i}"):
                actual = self.s.is_feasible(nums, m, i)
                self.assertEqual(actual, expects[i])

    def test_is_feasible3(self):
        nums = [7,2,5,10,8]
        m = 2
        expects = {16: False, 17: False, 18: True, 19:True}
        for i in range(16, 20):
            with self.subTest(f"Testing nums={nums}, m={m}, largest_sum={i}"):
                actual = self.s.is_feasible(nums, m, i)
                self.assertEqual(actual, expects[i])

    def test_case1(self):
        nums = [7,2,5,10,8]
        m = 2
        actual = self.s.splitArray(nums, m)
        self.assertEqual(18, actual)

    def test_case2(self):
        nums = [1,2,3,4,5]
        m = 2
        actual = self.s.splitArray(nums, m)
        self.assertEqual(9, actual)

    def test_case3(self):
        nums = [1,4, 4]
        m = 3
        actual = self.s.splitArray(nums, m)
        self.assertEqual(4, actual)

    def test_case4(self):
        nums = [1]
        m = 1
        actual = self.s.splitArray(nums, m)
        self.assertEqual(1, actual)

    def test_case5(self):
        nums = [1, 2]
        m = 2
        actual = self.s.splitArray(nums, m)
        self.assertEqual(2, actual)

    def test_case6(self):
        nums = [1, 6, 4, 1, 2]
        m = 3
        actual = self.s.splitArray(nums, m)
        self.assertEqual(7, actual)


if __name__ == '__main__':
    unittest.main()

