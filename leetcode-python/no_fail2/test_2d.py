import unittest
from .challenge_2d import solve2


class MyTestCase(unittest.TestCase):
    def test_case_1(self):
        lines = """3 2
2 4 1""".split("\n")

        n_k = list(map(int, lines[0].split(' ')))
        k = n_k[1]
        numbers = list(map(int, lines[1].split(' ')))

        print(numbers)
        print(k)
        result = solve2(numbers, k)
        self.assertEqual(result, 2)
