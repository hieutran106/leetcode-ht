import unittest
from .challenge_2 import solution, parse_input

class MyTestCase(unittest.TestCase):
    def test_case_1(self):
        my_input = """4 4
        0100
        0001
        0011
        1110
        """
        grid = parse_input(my_input)
        result = solution(grid)
        self.assertEqual(result, 6)

    def test_case_2(self):
        my_input = """4 5
        00010
        11011
        00100
        00001
        """
        grid = parse_input(my_input)
        result = solution(grid)
        self.assertEqual(result, 3)

    def test_case_3(self):
        my_input = """1 1
        00000000
        """
        grid = parse_input(my_input)
        result = solution(grid)
        self.assertEqual(result, 0)




if __name__ == '__main__':
    unittest.main()
