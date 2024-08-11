import unittest
from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        directions = [
            ('Right', 0, 1),
            ('Down', 1, 0),
            ('Left', 0, -1),
            ('Up', -1, 0)
        ]
        direction_index = 0

        rows = len(matrix)
        cols = len(matrix[0])

        first_left = False
        first_right = False
        horizontal = None
        vertical = None

        def get_steps(direction):
            nonlocal first_left
            nonlocal horizontal
            nonlocal first_right
            nonlocal vertical
            if direction == 'Left':
                if not first_left:
                    first_left = True
                    horizontal = cols - 1
                else:
                    horizontal = horizontal - 1
                return horizontal
            elif direction == "Right":
                if not first_right:
                    first_right = True
                    horizontal = cols - 1
                else:
                    horizontal = horizontal - 1
                return horizontal
            else:
                vertical = vertical -1 if vertical is not None else rows - 1
                return vertical


        curr_row = 0
        curr_col = 0
        ans = [matrix[curr_row][curr_col]]
        while len(ans) < rows * cols:
            direction, dx, dy = directions[direction_index]
            steps = get_steps(direction)
            print(f"Walk {direction} in {steps} steps")
            for i in range(steps):
                curr_row = curr_row + dx
                curr_col = curr_col + dy
                ans.append(matrix[curr_row][curr_col])
                if len(ans) == rows * cols:
                    break
            direction_index = direction_index + 1 if direction_index < 3 else 0
        return ans


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        actual = self.s.spiralOrder(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        self.assertEqual([1, 2, 3, 6, 9, 8, 7, 4, 5], actual)

    def test_case_2(self):
        actual = self.s.spiralOrder(matrix=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
        self.assertEqual([1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7], actual)

    def test_case_3(self):
        actual = self.s.spiralOrder(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
        self.assertEqual([1, 2, 3, 6, 9, 12, 15, 18, 17, 16, 13, 10, 7, 4, 5, 8, 11, 14], actual)

    def test_case_4(self):
        actual = self.s.spiralOrder(matrix=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
        self.assertEqual([1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10], actual)

    def test_case_5(self):
        actual = self.s.spiralOrder(
            matrix=[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20],
                    [21, 22, 23, 24, 25]])
        self.assertEqual([1, 2, 3, 4, 5, 10, 15, 20, 25, 24, 23, 22, 21, 16, 11, 6, 7, 8, 9, 14, 19, 18, 17, 12, 13],
                         actual)


if __name__ == '__main__':
    unittest.main()
