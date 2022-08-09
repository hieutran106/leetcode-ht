import unittest
from .challenge_2a import solution, solve_case


class MyTestCase(unittest.TestCase):
    def test_case_1(self):
        my_input = """6
6
1 4 7 9001 2 15000
3
1 2 10
10
1024 1 16 32 1 999 123 321 9 15
30
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
9
8 1 10 22 75 121 4 73 335
4
8 1 10 22"""

#         my_input = """1
# 3
# 1 2 10
# 9
# 8 1 10 22 75 121 4 73 335"""
        my_input = my_input.split("\n")
        my_input = my_input[1:]
        solution(my_input)