import unittest
from typing import List


class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        def is_inside(r, c):
            return 0 <= r < rows and 0 <= c < cols

        directions = [
            ('Right', 0, 1),
            ('Down', 1, 0),
            ('Left', 0, -1),
            ('Up', -1, 0)
        ]
        ans = [[rStart, cStart]]
        direction_index = 0
        direction = directions[direction_index]
        step = 0
        curr_row = rStart
        curr_col = cStart
        while len(ans) < rows * cols:
            print("================================")
            dir_name, dx, dy = direction
            if dir_name == 'Right' or dir_name == 'Left':
                step += 1
            print(f"Walk {dir_name} for {step} steps")
            for i in range(step):
                curr_row = curr_row + dx
                curr_col = curr_col + dy
                if is_inside(curr_row, curr_col):
                    ans.append([curr_row, curr_col])
            # next direction
            direction_index = direction_index + 1 if direction_index < 3 else 0
            direction = directions[direction_index]

        return ans


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        actual = self.s.spiralMatrixIII(rows=1, cols=4, rStart=0, cStart=0)
        self.assertEqual([[0, 0], [0, 1], [0, 2], [0, 3]], actual)

    def test_case_2(self):
        actual = self.s.spiralMatrixIII(rows=5, cols=6, rStart=1, cStart=4)
        self.assertEqual(
            [[1, 4], [1, 5], [2, 5], [2, 4], [2, 3], [1, 3], [0, 3], [0, 4], [0, 5], [3, 5], [3, 4], [3, 3], [3, 2],
             [2, 2], [1, 2], [0, 2], [4, 5], [4, 4], [4, 3], [4, 2], [4, 1], [3, 1], [2, 1], [1, 1], [0, 1], [4, 0],
             [3, 0], [2, 0], [1, 0], [0, 0]], actual)


if __name__ == '__main__':
    unittest.main()
