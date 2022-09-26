import unittest
from .solution import MyCalendarTwo

class MyTestCase(unittest.TestCase):


    def test_case_1(self):
        calendar = MyCalendarTwo()
        actual = calendar.book(10, 20)
        self.assertEqual(True, actual)

        actual = calendar.book(50, 60)
        self.assertEqual(True, actual)

        actual = calendar.book(10, 40)
        self.assertEqual(True, actual)

        actual = calendar.book(5, 15)
        self.assertEqual(False, actual)

        actual = calendar.book(25, 55)
        self.assertEqual(True, actual)

    def test_case_2(self):
        calendar = MyCalendarTwo()
        actual = calendar.book(10, 20)
        self.assertEqual(True, actual)

        actual = calendar.book(30, 40)
        self.assertEqual(True, actual)

        actual = calendar.book(25, 35)
        self.assertEqual(True, actual)

if __name__ == '__main__':
    unittest.main()

