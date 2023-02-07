import unittest
from .solution import Solution


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        actual = self.s.canFinish(numCourses=2, prerequisites=[[1, 0]])
        self.assertEqual(True, actual)

    def test_case_2(self):
        actual = self.s.canFinish(numCourses=2, prerequisites=[[1, 0], [0, 1]])
        self.assertEqual(False, actual)

    def test_case_3(self):
        actual = self.s.canFinish(numCourses=3, prerequisites=[[1, 0], [0, 1], [2, 1]])
        self.assertEqual(False, actual)

    def test_case_4(self):
        actual = self.s.canFinish(numCourses=5, prerequisites=[[1,4],[2,4],[3,1],[3,2]])
        self.assertEqual(True, actual)


if __name__ == '__main__':
    unittest.main()
