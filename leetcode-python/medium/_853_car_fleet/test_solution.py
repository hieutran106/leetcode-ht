import unittest
from .solution import Solution


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        target = 12
        position = [10, 8, 0, 5, 3]
        speed = [2, 4, 1, 1, 3]
        actual = self.s.carFleet(target, position, speed)
        self.assertEqual(actual, 3)

    def test_case_2(self):
        target = 10
        position = [3]
        speed = [3]
        actual = self.s.carFleet(target, position, speed)
        self.assertEqual(actual, 1)

    def test_case_3(self):
        target = 100
        position = [0, 2, 4]
        speed = [4, 2, 1]
        actual = self.s.carFleet(target, position, speed)
        self.assertEqual(actual, 1)

    def test_case_4(self):
        target = 10
        position = [0, 4, 2]
        speed = [2, 1, 3]
        actual = self.s.carFleet(target, position, speed)
        self.assertEqual(actual, 1)


if __name__ == '__main__':
    unittest.main()
