import unittest
from .solution import DetectSquares

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = DetectSquares()

    def test_case_1(self):
        self.s.add([3, 10])
        self.s.add([11, 2])
        self.s.add([3, 2])
        actual = self.s.count([11, 10])
        self.assertEqual(actual, 1)

    def test_case_2(self):
        self.s.add([3, 10])
        self.s.add([11, 2])
        self.s.add([3, 2])
        actual = self.s.count([14, 8]);
        self.assertEqual(actual, 0)

    def test_case_3(self):
        self.s.add([3, 10])
        self.s.add([11, 2])
        self.s.add([3, 2])
        self.s.add([11, 2])
        actual = self.s.count([11, 10]);
        self.assertEqual(actual, 2)

    def test_case_4(self):
        self.s.add([5, 10])
        self.s.add([10, 5])
        self.s.add([10, 10])
        self.assertEqual(self.s.count([5, 5]), 1)
        self.s.add([3, 0])
        self.s.add([8, 0])
        self.s.add([8, 5])
        self.assertEqual(self.s.count([3, 5]), 1)
        self.s.add([9, 0])
        self.s.add([9, 8])
        self.s.add([1, 8])
        self.assertEqual(self.s.count([1, 0]), 1)
        self.s.add([0, 0])
        self.s.add([8, 0])
        self.s.add([8, 8])
        self.assertEqual(self.s.count([0, 8]), 2)

    def test_case_5(self):
        self.s.add([5, 10])
        self.s.add([10, 5])
        self.s.add([10, 10])
        # self.assertEqual(self.s.count([5, 5]), 1)
        self.s.add([3, 0])
        self.s.add([8, 0])
        self.s.add([8, 5])
        # self.assertEqual(self.s.count([3, 5]), 1)
        self.s.add([9, 0])
        self.s.add([9, 8])
        self.s.add([1, 8])
        # self.assertEqual(self.s.count([1, 0]), 1)
        self.s.add([0, 0])
        self.s.add([8, 0])
        self.s.add([8, 8])
        # self.assertEqual(self.s.count([0, 8]), 2)
        self.s.add([1, 9])
        self.s.add([2, 9])
        self.s.add([2, 10])
        # self.assertEqual(self.s.count([1, 10]), 1)
        self.s.add([7, 8])
        self.s.add([2, 3])
        self.s.add([2, 8])
        # self.assertEqual(self.s.count([7, 3]), 1)
        self.s.add([9, 10])
        self.s.add([9, 5])
        self.s.add([4, 5])
        # self.assertEqual(self.s.count([4, 10]), 1)
        self.s.add([0, 9])
        self.s.add([4, 5])
        self.s.add([4, 9])
        # self.assertEqual(self.s.count([0, 5]), 2)
        self.s.add([1, 10])
        self.s.add([10, 1])
        self.s.add([10, 10])
        # self.assertEqual(self.s.count([1, 1]), 2)
        self.s.add([10, 0])
        self.s.add([2, 0])
        self.s.add([2, 8])
        # self.assertEqual(self.s.count([10, 8]), 2)
        self.s.add([7, 6])
        self.s.add([4, 6])
        self.s.add([4, 9])
        # self.assertEqual(self.s.count([7, 9]), 2)
        self.s.add([10, 9])
        self.s.add([10, 0])
        self.s.add([1, 0])
        self.assertEqual(self.s.count([1, 9]), 5)
        self.s.add([0, 9])
        self.s.add([8, 1])
        self.s.add([0, 1])
        self.assertEqual(self.s.count([8, 9]), 6)
        self.s.add([3, 9])
        self.s.add([10, 9])
        self.s.add([3, 2])
        self.assertEqual(self.s.count([10, 2]), 2)
        self.s.add([3, 8])
        self.s.add([9, 2])
        self.s.add([3, 2])
        self.assertEqual(self.s.count([9, 8]), 3)
        self.s.add([0, 9])
        self.s.add([7, 9])
        self.s.add([0, 2])
        self.assertEqual(self.s.count([7, 2]), 3)
        self.s.add([10, 1])
        self.s.add([1, 10])
        self.s.add([10, 10])
        self.assertEqual(self.s.count([1, 1]), 14)
        self.s.add([6, 10])
        self.s.add([2, 6])
        self.s.add([6, 6])
        self.assertEqual(self.s.count([2, 10]), 3)
        self.s.add([6, 0])
        self.s.add([6, 2])
        self.s.add([8, 2])
        self.assertEqual(self.s.count([8, 0]), 1)
        self.s.add([6, 5])
        self.s.add([7, 4])
        self.s.add([6, 4])
        self.assertEqual(self.s.count([7, 5]), 2)
        self.s.add([2, 10])
        self.s.add([8, 4])
        self.s.add([2, 4])
        self.assertEqual(self.s.count([8, 10]), 2)
        self.s.add([2, 6])
        self.s.add([2, 5])
        self.s.add([1, 5])
        self.assertEqual(self.s.count([1, 6]), 4)
        self.s.add([10, 9])
        self.s.add([10, 0])
        self.s.add([1, 9])
        self.assertEqual(self.s.count([1, 0]), 20)
        self.s.add([0, 9])
        self.s.add([5, 9])
        self.s.add([0, 4])
        self.assertEqual(self.s.count([5, 4]), 4)
        self.s.add([3, 6])
        self.s.add([9, 0])
        self.s.add([3, 0])
        self.assertEqual(self.s.count([9, 6]), 5)
        self.s.add([0, 2])
        self.s.add([1, 1])
        self.s.add([0, 1])
        self.assertEqual(self.s.count([1, 2]), 10)
        self.s.add([1, 7])
        self.s.add([8, 0])
        self.s.add([8, 7])
        self.assertEqual(self.s.count([1, 0]), 26)
        self.s.add([2, 7])
        self.s.add([4, 5])
        self.s.add([2, 5])
        self.assertEqual(self.s.count([4, 7]), 8)
        self.s.add([6, 7])
        self.s.add([3, 7])
        self.s.add([6, 4])
        self.assertEqual(self.s.count([3, 4]), 3)
        self.s.add([10, 2])
        self.s.add([2, 10])
        self.s.add([2, 2])
        self.assertEqual(self.s.count([10, 10]), 7)
        self.s.add([10, 1])
        self.s.add([1, 10])
        self.s.add([1, 1])
        self.assertEqual(self.s.count([10, 10]), 21)
        self.s.add([2, 10])
        self.s.add([2, 9])
        self.s.add([3, 9])
        self.assertEqual(self.s.count([3, 10]), 20)
        self.s.add([10, 1])
        self.s.add([1, 10])
        self.s.add([1, 1])
        self.assertEqual(self.s.count([10, 10]), 52)
        self.s.add([10, 4])
        self.s.add([10, 3])
        self.s.add([9, 4])
        self.assertEqual(self.s.count([9, 3]), 6)
        self.s.add([6, 6])
        self.s.add([6, 10])
        self.s.add([10, 6])
        self.assertEqual(self.s.count([10, 10]), 56)
        self.s.add([9, 7])
        self.s.add([4, 7])
        self.s.add([9, 2])
        self.assertEqual(self.s.count([4, 2]), 2)
        self.s.add([2, 3])
        self.s.add([2, 1])
        self.s.add([0, 3])
        self.assertEqual(self.s.count([0, 1]), 5)
        self.s.add([2, 8])
        self.s.add([10, 8])
        self.s.add([2, 0])
        self.assertEqual(self.s.count([10, 0]), 17)
        self.s.add([8, 4])
        self.s.add([2, 10])
        self.s.add([8, 10])
        self.assertEqual(self.s.count([2, 4]), 18)
        self.s.add([0, 0])
        self.s.add([9, 9])
        self.s.add([0, 9])
        self.assertEqual(self.s.count([9, 0]), 13)
        self.s.add([5, 7])
        self.s.add([5, 8])
        self.s.add([4, 7])
        self.assertEqual(self.s.count([4, 8]), 19)
        self.s.add([10, 10])
        self.s.add([10, 1])
        self.s.add([1, 1])
        self.assertEqual(self.s.count([1, 10]), 102)
        self.s.add([6, 8])
        self.s.add([7, 8])
        self.s.add([6, 9])
        self.assertEqual(self.s.count([7, 9]), 9)
        self.s.add([4, 6])
        self.s.add([1, 6])
        self.s.add([4, 3])
        self.assertEqual(self.s.count([1, 3]), 2)
        self.s.add([10, 1])
        self.s.add([1, 10])
        self.s.add([10, 10])
        self.assertEqual(self.s.count([1, 1]), 157)
        self.s.add([7, 7])
        self.s.add([7, 10])
        self.s.add([4, 7])
        self.assertEqual(self.s.count([4, 10]), 23)
        self.s.add([0, 0])
        self.s.add([8, 0])
        self.s.add([0, 8])
        self.assertEqual(self.s.count([8, 8]), 29)
        self.s.add([3, 5])
        self.s.add([2, 4])
        self.s.add([3, 4])
        self.assertEqual(self.s.count([2, 5]), 23)
        self.s.add([0, 6])
        self.s.add([0, 2])
        self.s.add([4, 2])
        self.assertEqual(self.s.count([4, 6]), 15)
        self.s.add([5, 2])
        self.s.add([9, 6])
        self.s.add([9, 2])
        self.assertEqual(self.s.count([5, 6]), 24)
        self.s.add([1, 1])
        self.s.add([1, 10])
        self.s.add([10, 10])
        self.assertEqual(self.s.count([10, 1]), 186)
        self.s.add([7, 5])
        self.s.add([2, 0])
        self.s.add([2, 5])
        self.assertEqual(self.s.count([7, 0]), 12)
        self.s.add([1, 9])
        self.s.add([1, 2])
        self.s.add([8, 2])
        self.assertEqual(self.s.count([8, 9]), 32)
        self.s.add([3, 8])
        self.s.add([3, 3])
        self.s.add([8, 3])
        self.assertEqual(self.s.count([8, 8]), 36)
        self.s.add([3, 10])
        self.s.add([9, 10])
        self.s.add([3, 4])
        self.assertEqual(self.s.count([9, 4]), 10)
        self.s.add([0, 2])
        self.s.add([0, 10])
        self.s.add([8, 10])
        self.assertEqual(self.s.count([8, 2]), 35)
        self.s.add([9, 4])
        self.s.add([8, 4])
        self.s.add([8, 5])
        self.assertEqual(self.s.count([9, 5]), 20)
        self.s.add([9, 8])
        self.s.add([4, 3])
        self.s.add([4, 8])
        self.assertEqual(self.s.count([9, 3]), 43)
        self.s.add([4, 9])
        self.s.add([0, 5])
        self.s.add([0, 9])
        self.assertEqual(self.s.count([4, 5]), 48)
        self.s.add([1, 3])
        self.s.add([3, 5])
        self.s.add([1, 5])
        self.assertEqual(self.s.count([3, 3]), 35)
        self.s.add([0, 0])
        self.s.add([0, 8])
        self.s.add([8, 0])
        self.assertEqual(self.s.count([8, 8]), 73)
        self.s.add([2, 8])
        self.s.add([10, 0])
        self.s.add([10, 8])
        self.assertEqual(self.s.count([2, 0]), 59)
        self.s.add([8, 1])
        self.s.add([0, 9])
        self.s.add([8, 9])
        self.assertEqual(self.s.count([0, 1]), 56)
        self.s.add([4, 9])
        self.s.add([4, 6])
        self.s.add([1, 9])
        self.assertEqual(self.s.count([1, 6]), 72)
        self.s.add([0, 9])
        self.s.add([0, 8])
        self.s.add([1, 9])
        self.assertEqual(self.s.count([1, 8]), 198)
        self.s.add([5, 1])
        self.s.add([5, 6])
        self.s.add([10, 1])
        self.assertEqual(self.s.count([10, 6]), 37)
        self.s.add([9, 2])
        self.s.add([2, 2])
        self.s.add([2, 9])
        self.assertEqual(self.s.count([9, 9]), 145)
        self.s.add([5, 5])
        self.s.add([8, 5])
        self.s.add([5, 8])
        self.assertEqual(self.s.count([8, 8]), 130)
        self.s.add([8, 0])
        self.s.add([1, 0])
        self.s.add([8, 7])
        self.assertEqual(self.s.count([1, 7]), 45)
        self.s.add([8, 2])
        self.s.add([5, 5])
        self.s.add([5, 2])
        self.assertEqual(self.s.count([8, 5]), 68)
        self.s.add([6, 6])
        self.s.add([6, 8])
        self.s.add([8, 6])
        self.assertEqual(self.s.count([8, 8]), 172)
        self.s.add([2, 10])
        self.s.add([10, 2])
        self.s.add([2, 2])
        self.assertEqual(self.s.count([10, 10]), 281)
        self.s.add([1, 9])
        self.s.add([8, 2])
        self.s.add([1, 2])
        self.assertEqual(self.s.count([8, 9]), 147)
        self.s.add([7, 4])
        self.s.add([7, 2])
        self.s.add([9, 4])
        self.assertEqual(self.s.count([9, 2]), 53)
        self.s.add([1, 9])
        self.s.add([1, 0])
        self.s.add([10, 0])
        self.assertEqual(self.s.count([10, 9]), 160)
        self.s.add([2, 10])
        self.s.add([2, 3])
        self.s.add([9, 10])
        self.assertEqual(self.s.count([9, 3]), 105)
        self.s.add([10, 0])
        self.s.add([1, 0])
        self.s.add([1, 9])
        self.assertEqual(self.s.count([10, 9]), 253)
        self.s.add([8, 10])
        self.s.add([1, 10])
        self.s.add([1, 3])
        self.assertEqual(self.s.count([8, 3]), 82)
        self.s.add([0, 9])
        self.s.add([9, 9])
        self.s.add([0, 0])
        self.assertEqual(self.s.count([9, 0]), 103)
        self.s.add([7, 9])
        self.s.add([8, 9])
        self.s.add([7, 8])
        self.assertEqual(self.s.count([8, 8]), 248)
        self.s.add([3, 1])
        self.s.add([9, 7])
        self.s.add([9, 1])
        self.assertEqual(self.s.count([3, 7]), 75)
        self.s.add([5, 9])
        self.s.add([6, 9])
        self.s.add([5, 8])
        self.assertEqual(self.s.count([6, 8]), 86)
        self.s.add([0, 1])
        self.s.add([0, 10])
        self.s.add([9, 10])
        self.assertEqual(self.s.count([9, 1]), 312)
        self.s.add([8, 0])
        self.s.add([8, 2])
        self.s.add([10, 2])
        self.assertEqual(self.s.count([10, 0]), 301)
        self.s.add([8, 0])
        self.s.add([0, 8])
        self.s.add([8, 8])
        self.assertEqual(self.s.count([0, 0]), 273)
        self.s.add([6, 7])
        self.s.add([5, 8])
        self.s.add([5, 7])
        self.assertEqual(self.s.count([6, 8]), 119)
        self.s.add([0, 9])
        self.s.add([0, 2])
        self.s.add([7, 9])
        self.assertEqual(self.s.count([7, 2]), 191)
        self.s.add([5, 0])
        self.s.add([5, 5])
        self.s.add([10, 0])
        self.assertEqual(self.s.count([10, 5]), 61)
        self.s.add([1, 10])
        self.s.add([10, 10])
        self.s.add([10, 1])
        self.assertEqual(self.s.count([1, 1]), 584)
        self.s.add([9, 2])
        self.s.add([9, 10])
        self.s.add([1, 2])
        self.assertEqual(self.s.count([1, 10]), 696)
        self.s.add([1, 10])
        self.s.add([10, 1])
        self.s.add([10, 10])
        self.assertEqual(self.s.count([1, 1]), 802)
        self.s.add([9, 9])
        self.s.add([0, 9])
        self.s.add([0, 0])
        self.assertEqual(self.s.count([9, 0]), 293)
        self.s.add([9, 6])
        self.s.add([9, 3])
        self.s.add([6, 3])
        self.assertEqual(self.s.count([6, 6]), 104)
        self.s.add([10, 4])
        self.s.add([6, 0])
        self.s.add([10, 0])
        self.assertEqual(self.s.count([6, 4]), 114)
        self.s.add([6, 8])
        self.s.add([0, 2])
        self.s.add([0, 8])
        self.assertEqual(self.s.count([6, 2]), 242)
        self.s.add([7, 9])
        self.s.add([0, 9])
        self.s.add([7, 2])
        self.assertEqual(self.s.count([0, 2]), 259)
        self.s.add([9, 1])
        self.s.add([9, 10])
        self.s.add([0, 10])
        self.assertEqual(self.s.count([0, 1]), 300)
        self.s.add([10, 0])
        self.s.add([10, 9])
        self.s.add([1, 9])
        self.assertEqual(self.s.count([1, 0]), 465)
        self.s.add([1, 6])
        self.s.add([1, 9])
        self.s.add([4, 9])
        self.assertEqual(self.s.count([4, 6]), 180)
        self.s.add([0, 8])
        self.s.add([1, 9])
        self.s.add([0, 9])
        self.assertEqual(self.s.count([1, 8]), 1082)
        self.s.add([1, 1])
        self.s.add([9, 1])
        self.s.add([1, 9])
        self.assertEqual(self.s.count([9, 9]), 697)
        self.s.add([2, 5])
        self.s.add([2, 9])
        self.s.add([6, 5])
        self.assertEqual(self.s.count([6, 9]), 187)
        self.s.add([7, 3])
        self.s.add([2, 3])
        self.s.add([2, 8])
        self.assertEqual(self.s.count([7, 8]), 113)
        self.s.add([9, 4])
        self.s.add([4, 4])
        self.s.add([9, 9])
        self.assertEqual(self.s.count([4, 9]), 201)
        self.s.add([4, 4])
        self.s.add([2, 4])
        self.s.add([4, 2])
        self.assertEqual(self.s.count([2, 2]), 520)
        self.s.add([0, 3])
        self.s.add([0, 2])
        self.s.add([1, 3])
        self.assertEqual(self.s.count([1, 2]), 652)
        self.s.add([10, 9])
        self.s.add([10, 2])
        self.s.add([3, 2])
        self.assertEqual(self.s.count([3, 9]), 197)
        self.s.add([5, 6])
        self.s.add([10, 6])
        self.s.add([10, 1])
        self.assertEqual(self.s.count([5, 1]), 91)
        self.s.add([9, 0])
        self.s.add([0, 9])
        self.s.add([9, 9])
        self.assertEqual(self.s.count([0, 0]), 670)
        self.s.add([5, 6])
        self.s.add([9, 2])
        self.s.add([9, 6])
        self.assertEqual(self.s.count([5, 2]), 159)
        self.s.add([3, 3])
        self.s.add([10, 3])
        self.s.add([10, 10])
        self.assertEqual(self.s.count([3, 10]), 189)
        self.s.add([2, 4])
        self.s.add([2, 10])
        self.s.add([8, 4])
        self.assertEqual(self.s.count([8, 10]), 386)
        self.s.add([4, 9])
        self.s.add([1, 9])
        self.s.add([4, 6])
        self.assertEqual(self.s.count([1, 6]), 403)
        self.s.add([1, 8])
        self.s.add([9, 0])
        self.s.add([1, 0])
        self.assertEqual(self.s.count([9, 8]), 204)
        self.s.add([10, 3])
        self.s.add([5, 8])
        self.s.add([5, 3])
        self.assertEqual(self.s.count([10, 8]), 301)
        self.s.add([8, 2])
        self.s.add([0, 10])
        self.s.add([8, 10])
        self.assertEqual(self.s.count([0, 2]), 378)
        self.s.add([9, 0])
        self.s.add([2, 7])
        self.s.add([9, 7])
        self.assertEqual(self.s.count([2, 0]), 314)
        self.s.add([0, 4])
        self.s.add([5, 9])
        self.s.add([0, 9])
        self.assertEqual(self.s.count([5, 4]), 292)
        self.s.add([5, 3])
        self.s.add([10, 3])
        self.s.add([5, 8])
        self.assertEqual(self.s.count([10, 8]), 352)
        self.s.add([6, 4])
        self.s.add([7, 4])
        self.s.add([6, 5])
        self.assertEqual(self.s.count([7, 5]), 174)
        self.s.add([9, 1])
        self.s.add([0, 1])
        self.s.add([9, 10])
        self.assertEqual(self.s.count([0, 10]), 2778)
        self.s.add([5, 10])
        self.s.add([5, 7])
        self.s.add([8, 7])
        self.assertEqual(self.s.count([8, 10]), 473)
        self.s.add([8, 0])
        self.s.add([8, 7])
        self.s.add([1, 7])
        self.assertEqual(self.s.count([1, 0]), 869)
        self.s.add([1, 1])
        self.s.add([9, 9])
        self.s.add([1, 9])
        self.assertEqual(self.s.count([9, 1]), 1568)
        self.s.add([3, 1])
        self.s.add([3, 5])
        self.s.add([7, 5])
        self.assertEqual(self.s.count([7, 1]), 190)
        self.s.add([5, 8])
        self.s.add([5, 3])
        self.s.add([10, 8])
        self.assertEqual(self.s.count([10, 3]), 198)
        self.s.add([0, 9])
        self.s.add([2, 7])
        self.s.add([2, 9])
        self.assertEqual(self.s.count([0, 7]), 342)
        self.s.add([9, 3])
        self.s.add([9, 7])
        self.s.add([5, 3])
        self.assertEqual(self.s.count([5, 7]), 286)
        self.s.add([0, 0])
        self.s.add([9, 0])
        self.s.add([9, 9])
        self.assertEqual(self.s.count([0, 9]), 1062)
        self.s.add([6, 4])
        self.s.add([4, 2])
        self.s.add([4, 4])
        self.assertEqual(self.s.count([6, 2]), 475)
        self.s.add([1, 9])
        self.s.add([1, 5])
        self.s.add([5, 5])
        self.assertEqual(self.s.count([5, 9]), 354)
        self.s.add([7, 7])
        self.s.add([0, 7])
        self.s.add([0, 0])
        self.assertEqual(self.s.count([7, 0]), 174)
        self.s.add([1, 3])
        self.s.add([1, 9])
        self.s.add([7, 3])
        self.assertEqual(self.s.count([7, 9]), 574)
        self.s.add([0, 9])
        self.s.add([9, 9])
        self.s.add([9, 0])
        self.assertEqual(self.s.count([0, 0]), 1605)
        self.s.add([1, 8])
        self.s.add([3, 6])
        self.s.add([3, 8])
        self.assertEqual(self.s.count([1, 6]), 547)



if __name__ == '__main__':
    unittest.main()
