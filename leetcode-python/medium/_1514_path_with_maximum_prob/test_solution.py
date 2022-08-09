import unittest
from .solution import Solution
from .helper import MaxHeap
class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()


    def test_case1(self):
        n = 3
        edges = [[0, 1], [1, 2], [0, 2]]
        succProb = [0.5, 0.5, 0.2]
        start = 0
        end = 2
        actual = self.s.maxProbability(n, edges, succProb, start, end)
        self.assertEqual(actual, 0.25)

    def test_case2(self):
        n = 3
        edges = [[0,1],[1,2],[0,2]]
        succProb = [0.5,0.5,0.3]
        start = 0
        end = 2
        actual = self.s.maxProbability(n, edges, succProb, start, end)
        self.assertEqual(actual, 0.3)

    def test_case3(self):
        n = 2
        edges = []
        succProb = []
        start = 0
        end = 1
        actual = self.s.maxProbability(n, edges, succProb, start, end)
        self.assertEqual(actual, 0)


if __name__ == '__main__':
    unittest.main()

