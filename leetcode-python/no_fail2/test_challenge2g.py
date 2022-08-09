import unittest
from .challenge_2g import solve, get_infos


class MyTestCase(unittest.TestCase):
    def test_case_1(self):
        lines = """4 5
        .....
        s...*
        *****
        .e*..""".split("\n")

        matrix, source, rows, cols = get_infos(lines)

        result = solve(matrix, source, rows, cols)
        self.assertEqual(result, 3)

    def test_case_1(self):
        lines = """4 5
.....
s...*
*****
.e*..""".split("\n")

        matrix, source, rows, cols = get_infos(lines)

        result = solve(matrix, source, rows, cols)
        self.assertEqual(result, -1)