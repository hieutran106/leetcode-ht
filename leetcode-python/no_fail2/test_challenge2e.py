import unittest
from .challenge_2e import get_info, bfs, solve


class MyTestCase(unittest.TestCase):
    def test_case_1(self):
        lines = """4
1 2 2
1 3 5
4 3 3""".split("\n")

        graph, n, edges, sum = get_info(lines)
        total = solve(graph, n, edges, sum)
        self.assertEqual(total, 17)



    def test_case_2(self):
        lines = """2
1 2 3""".split("\n")

        graph, n, edges, sum = get_info(lines)
        total = solve(graph, n, edges, sum)
        self.assertEqual(total, 3)

    def test_case_3(self):
        lines = """3
1 2 4
3 2 5""".split("\n")

        graph, n, edges, sum = get_info(lines)
        total = solve(graph, n, edges, sum)
        self.assertEqual(total, 13)

    def test_case_4(self):
        lines = """5
1 2 1
2 3 1
3 4 1
4 5 1""".split("\n")

        graph, n, edges, sum = get_info(lines)
        total = solve(graph, n, edges, sum)
        self.assertEqual(total, 10)

    def test_case_5(self):
        lines = """4
1 2 2
2 3 1
3 4 2""".split("\n")

        graph, n, edges, sum = get_info(lines)
        total = solve(graph, n, edges, sum)
        self.assertEqual(total, 8)


    def test_case_6(self):
        lines = """2
1 2 1""".split("\n")

        graph, n, edges, sum = get_info(lines)
        total = solve(graph, n, edges, sum)
        self.assertEqual(total, 1)

    def test_case_7(self):
        lines = """5
1 2 1
1 3 2
3 4 3
3 5 4""".split("\n")

        graph, n, edges, sum = get_info(lines)
        total = solve(graph, n, edges, sum)
        self.assertEqual(total, 20)