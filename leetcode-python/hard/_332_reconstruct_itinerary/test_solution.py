import unittest
from .solution import Solution


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        actual = self.s.findItinerary(tickets=[["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]])
        self.assertEqual(["JFK", "MUC", "LHR", "SFO", "SJC"], actual)

    def test_case_2(self):
        actual = self.s.findItinerary(
            tickets=[["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]])
        self.assertEqual(["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"], actual)

    def test_case_3(self):
        actual = self.s.findItinerary(
            [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]])
        self.assertEqual(["JFK","NRT","JFK","KUL"], actual)


if __name__ == '__main__':
    unittest.main()
