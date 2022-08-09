import unittest
from .solution import Solution, SolutionDFS

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = SolutionDFS()

    def test_case1(self):
        image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
        sr = 1
        sc = 1
        newColor = 2
        actual = self.s.floodFill(image, sr, sc, newColor)
        expect = [[2,2,2],[2,2,0],[2,0,1]]
        self.assertEqual(expect, actual)

if __name__ == '__main__':
    unittest.main()

