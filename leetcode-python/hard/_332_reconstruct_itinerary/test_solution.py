import unittest

import collections
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        adjacency_list = collections.defaultdict(list)
        # initializing adjacency list
        adjacency_list = collections.defaultdict(list)
        for start, end in tickets:
            dest = adjacency_list[start]
            dest.append(end)

        n = len(tickets)
        path = ["JFK"]
        def backtrack(airport) -> bool:
            if len(path) == n + 1:
                return True
            temp = list(adjacency_list[airport])
            for idx, des in enumerate(temp):
                adjacency_list[airport].pop()



    def findItinerary1(self, tickets: List[List[str]]) -> List[str]:
        # initializing adjacency list
        adjacency_list = collections.defaultdict(list)
        for start, end in tickets:
            dest = adjacency_list[start]
            dest.append({
                "airport": end,
                "visited": False
            })
        # sort
        for airport, destinations in adjacency_list.items():
            destinations.sort(key=lambda d: d["airport"])
        # print(adjacency_list)

        n = len(tickets)
        path = ["JFK"]

        def backtrack(airport) -> bool:
            not_visited = list(filter(lambda d: d["visited"] is False, adjacency_list[airport]))
            if len(not_visited) == 0:
                return True if len(path) == n + 1 else False
            for next in not_visited:
                path.append(next["airport"])
                next["visited"] = True
                if backtrack(next["airport"]):
                    return True
                path.pop()
                next["visited"] = False
            return False

        backtrack("JFK")
        return path


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
            [["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]])
        self.assertEqual(["JFK", "NRT", "JFK", "KUL"], actual)

    def test_case_4(self):
        actual = self.s.findItinerary(tickets=
                                      [["EZE", "TIA"], ["EZE", "HBA"], ["AXA", "TIA"], ["JFK", "AXA"], ["ANU", "JFK"],
                                       ["ADL", "ANU"], ["TIA", "AUA"], ["ANU", "AUA"], ["ADL", "EZE"], ["ADL", "EZE"],
                                       ["EZE", "ADL"], ["AXA", "EZE"], ["AUA", "AXA"], ["JFK", "AXA"], ["AXA", "AUA"],
                                       ["AUA", "ADL"], ["ANU", "EZE"], ["TIA", "ADL"], ["EZE", "ANU"], ["AUA", "ANU"]])
        self.assertEqual(
            ["JFK", "AXA", "AUA", "ADL", "ANU", "AUA", "ANU", "EZE", "ADL", "EZE", "ANU", "JFK", "AXA", "EZE", "TIA",
             "AUA", "AXA", "TIA", "ADL", "EZE", "HBA"], actual)


if __name__ == '__main__':
    unittest.main()
