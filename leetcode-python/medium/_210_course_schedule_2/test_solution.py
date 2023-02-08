import unittest
from .solution import Solution


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        actual = self.s.findOrder(numCourses=2, prerequisites=[[1, 0]])
        self.assertEqual([0, 1], actual)

    def test_case_2(self):
        actual = self.s.findOrder(numCourses=4, prerequisites=[[1, 0], [2, 0], [3, 1], [3, 2]])
        self.assertEqual([0, 1, 2, 3], actual)

    def test_case_3(self):
        actual = self.s.findOrder(numCourses = 1, prerequisites = [])
        self.assertEqual([0], actual)

    def test_case_4(self):
        actual = self.s.findOrder(numCourses = 3, prerequisites = [[0,1], [1,2], [2,0]])
        self.assertEqual([], actual)

    def test_case_5(self):
        actual = self.s.findOrder(numCourses=2, prerequisites=[[0,1]])
        self.assertEqual([1, 0], actual)


if __name__ == '__main__':
    unittest.main()
