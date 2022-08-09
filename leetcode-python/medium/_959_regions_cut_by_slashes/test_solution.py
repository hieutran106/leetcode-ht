import unittest
from .solution import Solution


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def test_case1(self):
        input = [" /", "/ "]
        actual = self.s.regionsBySlashes(input)
        self.assertEqual(2, actual)

    def test_case2(self):
        input = [" /", "  "]
        actual = self.s.regionsBySlashes(input)
        self.assertEqual(1, actual)

    def test_case3(self):
        input = ["\\/", "/\\"]
        actual = self.s.regionsBySlashes(input)
        self.assertEqual(4, actual)

    def test_case4(self):
        input = ["/\\", "\\/"]
        actual = self.s.regionsBySlashes(input)
        self.assertEqual(5, actual)

    def test_case5(self):
        input = ["//", "/ "]
        actual = self.s.regionsBySlashes(input)
        self.assertEqual(3, actual)


    def test_case6(self):
        input = ["\\\\", "\\\\"]
        actual = self.s.regionsBySlashes(input)
        self.assertEqual(4, actual)

    def test_case7(self):
        input = ["\\\\", " \\"]
        actual = self.s.regionsBySlashes(input)
        self.assertEqual(3, actual)


if __name__ == "__main__":
    unittest.main()
