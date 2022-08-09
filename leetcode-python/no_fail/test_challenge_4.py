import unittest
from .challenge_4 import ferry_cost


class MyTestCase(unittest.TestCase):
    def test_case1(self):
        n = 4
        m = 4
        edges = [[0, 1, 2], [0, 3, 10], [1, 2, 7], [2, 3, 5]]
        actual = ferry_cost(edges, n)
        self.assertEqual(actual, 7)

    def test_case2(self):
        n = 5
        m = 3
        edges = [
            [0, 3, 5],
            [3, 4, 100],
            [1, 2, 4],
        ]
        actual = ferry_cost(edges, n)
        self.assertEqual(actual, 100)

    def test_case3(self):
        n = 5
        m = 5
        edges = [
            [0, 1, 10],
        ]
        actual = ferry_cost(edges, n)
        self.assertEqual(actual, -1)

    def test_case4(self):
        n = 6
        m = 4
        edges = [
            [0, 1, 1],
            [1, 4, 2],
            [4, 0, 1],
        ]
        actual = ferry_cost(edges, n)
        self.assertEqual(actual, -1)

    def test_case5(self):
        n = 6
        m = 4
        edges = [
            [0, 1, 1],
            [1, 4, 2],
            [4, 0, 1],
            [4, 5, 10],
            [5, 6, 1],
        ]
        actual = ferry_cost(edges, n)
        self.assertEqual(actual, 10)

    def test_case6(self):
        n = 4
        m = 4
        edges = [
            [0, 1, 3],
            [1, 3, 7],
            [0, 3, 10],
            [0, 2, 1],
            [2, 3, 8],
        ]
        actual = ferry_cost(edges, n)
        self.assertEqual(actual, 7)

    def test_case7(self):
        n = 5
        m = 3
        edges = [[0, 3, 4], [3, 4, 100], [1, 2, 4]]
        actual = ferry_cost(edges, n)
        self.assertEqual(actual, 100)

    def test_case8(self):
        n = 5
        edges = [
            [0, 1, 1],
            [0, 2, 1],
            [1, 2, 3],
            [1, 3, 2],
            [2, 4, 2],
            [4, 3, 2],
            [3, 5, 3],
            [4, 1, 5],
        ]
        actual = ferry_cost(edges, n)
        self.assertEqual(actual, 2)

    def test_case9(self):
        n = 6
        edges = [
            [0, 1, 1],
            [0, 2, 1],
            [1, 2, 2],
            [1, 3, 2],
            [2, 4, 2],
            [4, 3, 2],
        ]
        actual = ferry_cost(edges, n)
        self.assertEqual(actual, -1)

    def test_case_10(self):
        n = 4
        edges = [[0, 1, 10], [0, 2, 1], [1, 2, 12], [2, 3, 12], [1, 3, 14]]
        actual = ferry_cost(edges, n)
        self.assertEqual(actual, 12)

    def test_case_11(self):
        n = 6
        m = 8
        edges = [
            [0, 1, 5],
            [0, 2, 4],
            [1, 2, 3],
            [1, 3, 4],
            [2, 3, 7],
            [3, 5, 4],
            [4, 5, 12],
            [1, 4, 10],
        ]
        actual = ferry_cost(edges, n)
        self.assertEqual(actual, 4)

    def test_case_12(self):
        n = 6
        m = 8
        edges = [
            [0, 1, 5],
            [0, 2, 4],
            [1, 2, 3],
            [1, 3, 8],
            [2, 3, 7],
            [3, 5, 4],
            [4, 5, 12],
            [1, 4, 10],
        ]
        actual = ferry_cost(edges, n)
        self.assertEqual(actual, 7)

    def test_case_13(self):
        n = 5

        edges = [
            [0, 1, 5],
            [0, 2, 4],
            [1, 2, 3],
            [1, 3, 1],
            [1, 4, 7],
            [2, 3, 2],
            [3, 4, 8],
        ]
        actual = ferry_cost(edges, n)
        self.assertEqual(actual, 7)

    def test_case_14(self):
        n = 4
        edges = [
            [0, 1, 7],
            [0, 2, 4],
            [0, 3, 8],
            [1, 2, 5],
            [1, 3, 4],
            [2, 3, 6],
        ]

        actual = ferry_cost(edges, n)
        self.assertEqual(actual, 5)

    def test_case_15(self):
        n = 10
        edges = [
            [0, 1, 1],
            [0, 3, 1],
            [0, 4, 0.5],
            [1, 2, 2],
            [1, 7, 2],
            [2, 3, 2],
            [2, 6, 1],
            [3, 4, 2],
            [3, 5, 1],
            [4, 8, 0.5],
            [5, 6, 1],
            [5, 8, 1.5],
            [6, 7, 0.5],
            [6, 9, 1],
            [7, 9, 0.5],
            [8, 9, 0.5],
        ]

        actual = ferry_cost(edges, n)
        self.assertEqual(actual, 0.5)

    def test_case16(self):
        n = 5
        edges = [[0, 1, 2], [0, 3, 10], [1, 2, 7], [2, 3, 5], [3, 4, 1]]
        actual = ferry_cost(edges, n)
        self.assertEqual(actual, 7)

    def test_case17(self):
        n = 6
        edges = [
            [1, 0, 42],
            [2, 1, 24],
            [3, 1, 2],
            [4, 2, 29],
            [5, 2, 41],
            [4, 1, 15],
            [3, 2, 26],
            [3, 0, 15],
            [2, 0, 29],
            [5, 0, 35],
            [5, 4, 18],
            [5, 3, 34],
            [4, 0, 28],
        ]
        actual = ferry_cost(edges, n)
        self.assertEqual(actual, 18)


if __name__ == "__main__":
    unittest.main()
