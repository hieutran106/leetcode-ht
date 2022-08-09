import unittest
from .solution import Solution


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def test_is_feasible1(self):
        bloomDay = [1, 10, 3, 10, 2]
        m = 3
        k = 1
        expects = {1: False, 2: False, 3: True, 4: True, 5: True}
        min_val = min(expects.keys())
        max_val = max(expects.keys())
        for i in range(min_val, max_val + 1):
            with self.subTest(f"Testing bloomDay={bloomDay}, m={m}, k={k}, days={i}"):
                actual = self.s.can_make(bloomDay, m, k, i)
                self.assertEqual(actual, expects[i])

    def test_is_feasible2(self):
        bloomDay = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]
        m = 4
        k = 2
        expects = {7: False, 8: False, 9: True, 10: True, 11: True}
        min_val = min(expects.keys())
        max_val = max(expects.keys())
        for i in range(min_val, max_val + 1):
            with self.subTest(f"Testing bloomDay={bloomDay}, m={m}, k={k}, days={i}"):
                actual = self.s.can_make(bloomDay, m, k, i)
                self.assertEqual(actual, expects[i])

    def test_case1(self):
        bloomDay = [1, 10, 3, 10, 2]
        m = 3
        k = 1
        actual = self.s.minDays(bloomDay, m, k)
        self.assertEqual(3, actual)

    def test_case2(self):
        bloomDay = [1, 10, 3, 10, 2]
        m = 3
        k = 2
        actual = self.s.minDays(bloomDay, m, k)
        self.assertEqual(-1, actual)

    def test_case3(self):
        bloomDay = [7, 7, 7, 7, 12, 7, 7]
        m = 2
        k = 3
        actual = self.s.minDays(bloomDay, m, k)
        self.assertEqual(12, actual)

    def test_case4(self):
        bloomDay = [1000000000, 1000000000]
        m = 1
        k = 1
        actual = self.s.minDays(bloomDay, m, k)
        self.assertEqual(1000000000, actual)

    def test_case5(self):
        bloomDay = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]
        m = 4
        k = 2
        actual = self.s.minDays(bloomDay, m, k)
        self.assertEqual(9, actual)


if __name__ == "__main__":
    unittest.main()
