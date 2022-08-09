import unittest
from .challenge_5 import main, build_segment_tree, get_sum
import inspect

class MyTestCase(unittest.TestCase):
    def test_case_1(self):
        raw_input = """6 9
        5 7 10 8 6 5
        0 2 4
        1 0 0 8
        0 1 3
        1 3 4 7
        0 1 1
        1 1 4 10
        0 3 3
        1 3 5 10
        0 0 2
        """

        output = """24
        25
        7
        25
        50"""
        processed_input = inspect.cleandoc(raw_input).split("\n")
        processed_output = inspect.cleandoc(output)

        actual = main(processed_input)
        self.assertEqual(actual, processed_output)

    def test_case_1(self):
        raw_input = """8 11
        10 7 10 7 3 10 7 2
        1 2 2 1
        0 0 1
        1 2 4 4
        0 1 7
        1 4 5 5
        1 4 5 1
        0 1 1
        1 3 4 1
        1 4 4 9
        1 1 1 3
        0 2 2
        """

        output = """17
        59
        7
        15"""
        processed_input = inspect.cleandoc(raw_input).split("\n")
        processed_output = inspect.cleandoc(output)

        actual = main(processed_input)
        self.assertEqual(actual, processed_output)

    def test_case_zero(self):
        array = [1, 3, 5, 7, 9, 11]
        root = build_segment_tree(array, 0, len(array) - 1)
        self.assertEqual(root.val, 36)

    def test_case_zero1(self):
        array = [1, 3, 5, 7, 9, 11]
        root = build_segment_tree(array, 0, len(array))
        actual = get_sum(root, 0, 5)
        self.assertEqual(actual, 36)

        actual = get_sum(root, 1, 4)
        self.assertEqual(actual, 24)

if __name__ == "__main__":
    unittest.main()
