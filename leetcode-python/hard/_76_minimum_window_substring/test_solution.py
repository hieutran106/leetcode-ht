import unittest
from .solution import Solution

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        actual = self.s.minWindow(s = "ADOBECODEBANC", t = "ABC")
        self.assertEqual(actual, "BANC")

    def test_case_2(self):
        actual = self.s.minWindow(s="a", t="a")
        self.assertEqual(actual, "a")

    def test_case_3(self):
        actual = self.s.minWindow(s="a", t="aa")
        self.assertEqual(actual, "")

    def test_case_4(self):
        actual = self.s.minWindow(s="a", t="b")
        self.assertEqual(actual, "")

    def test_case_5(self):
        actual = self.s.minWindow(s="ABCabDDDDDDcABBBB", t="abc")
        self.assertEqual(actual, "abDDDDDDc")

    def test_case_6(self):
        actual = self.s.minWindow(s="ABCabDDDDDDcABBBB", t="ab")
        self.assertEqual(actual, "ab")

    def test_case_7(self):
        actual = self.s.minWindow(s="abababbbbbaaaa", t="cd")
        self.assertEqual(actual, "")

    def test_case_8(self):
        actual = self.s.minWindow(s="xxabdc", t= "cba")
        self.assertEqual(actual, "abdc")

    def test_case_9(self):
        actual = self.s.minWindow(s="acbba", t="aab")
        self.assertEqual(actual, "acbba")


if __name__ == '__main__':
    unittest.main()

