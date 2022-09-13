import unittest
from .solution import Solution


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        actual = self.s.corpFlightBookings(bookings=[[1, 2, 10], [2, 3, 20], [2, 5, 25]], n=5)
        self.assertEqual(actual, [10, 55, 45, 25, 25])

    def test_case_2(self):
        actual = self.s.corpFlightBookings(bookings=[[1, 2, 10], [2, 2, 15]], n=2)
        self.assertEqual(actual, [10, 25])

    def test_case_3(self):
        actual = self.s.corpFlightBookings(bookings=[[1, 2, 10], [2, 4, 15]], n=4)
        self.assertEqual(actual, [10, 25, 15, 15])

    def test_case_4(self):
        actual = self.s.corpFlightBookings(bookings=[[2, 3, 10]], n=3)
        self.assertEqual(actual, [0, 10, 10])


if __name__ == '__main__':
    unittest.main()
