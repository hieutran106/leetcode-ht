import unittest
from .solution import Solution

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_is_feasible1(self):
        m = 3
        n = 3
        k = 5
        expects = {1: True, 2: True, 3: True, 4: False}
        min_val = min(expects.keys())
        max_val = max(expects.keys())
        for i in range(min_val, max_val + 1):
            with self.subTest(f"m={m}, n={n}, k={k}, values={i}"):
                actual = self.s.is_feasible(m, n, k, i)
                self.assertEqual(actual, expects[i])




    def test_is_feasible2(self):
        m = 5
        n = 5
        k = 8
        expects = {5: False, 4: True, 3: True}
        min_val = min(expects.keys())
        max_val = max(expects.keys())
        for i in range(min_val, max_val + 1):
            with self.subTest(f"m={m}, n={n}, k={k}, values={i}"):
                actual = self.s.is_feasible(m, n, k, i)
                self.assertEqual(actual, expects[i])


    def test_case1(self):
        m = 3
        n = 3
        k = 5
        actual = self.s.findKthNumber(m, n, k)
        self.assertEqual(3, actual)

    def test_case2(self):
        m = 2
        n = 3
        k = 6
        actual = self.s.findKthNumber(m, n, k)
        self.assertEqual(6, actual)


    def test_case3(self):
        m = 1
        n = 1
        k = 1
        actual = self.s.findKthNumber(m, n, k)
        self.assertEqual(1, actual)

    def test_case4(self):
        m = 5
        n = 5
        k = 6
        actual = self.s.findKthNumber(m, n, k)
        self.assertEqual(4, actual)

    def test_case5(self):
        m = 5
        n = 5
        k = 7
        actual = self.s.findKthNumber(m, n, k)
        self.assertEqual(4, actual)

    def test_case6(self):
        m = 5
        n = 5
        k = 9
        actual = self.s.findKthNumber(m, n, k)
        self.assertEqual(5, actual)

    def test_case7(self):
        m = 5
        n = 5
        k = 24
        actual = self.s.findKthNumber(m, n, k)
        self.assertEqual(20, actual)


    def test_case100(self):
        m = 9895
        n = 28405
        k = 100787757
        actual = self.s.findKthNumber(m, n, k)
        self.assertEqual(31666344, actual)

if __name__ == '__main__':
    unittest.main()


