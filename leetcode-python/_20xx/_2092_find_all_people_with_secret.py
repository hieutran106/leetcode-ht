import unittest
from typing import List
from utils.union_find import UnionFind
# Date: 2026-01-03
# Problem: 2092 find_all_people_with_secret
class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:

        uf = UnionFind(n)
        uf.union(0, firstPerson)

        # sort the meeting by time
        meetings.sort(key=lambda m: m[2])
        for p1, p2, time in meetings:
            if uf.connected(0, p1) or uf.connected(0, p2):
                uf.union(0, p1)
                uf.union(0, p2)

        ans = []
        for person, parent in enumerate(uf.parent):
            if parent == 0:
                ans.append(person)
        return ans
    

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        actual = self.s.findAllPeople(n=6, meetings=[[1, 2, 5], [2, 3, 8], [1, 5, 10]], firstPerson=1)
        self.assertEqual([0, 1, 2, 3, 5], actual)
        
    def test_case_2(self):
        actual = self.s.findAllPeople(n = 4, meetings = [[3,1,3],[1,2,2],[0,3,3]], firstPerson = 3)
        self.assertEqual([0, 1, 3], actual)

    def test_case_3(self):
        actual = self.s.findAllPeople(n = 5, meetings = [[3,4,2],[1,2,1],[2,3,1]], firstPerson = 1)
        self.assertEqual([0,1,2,3,4], actual)

    def test_case_4(self):
        actual = self.s.findAllPeople(n = 5, meetings = [[1,4,3],[0,4,3]], firstPerson = 3)
        self.assertEqual([0, 1, 3, 4], actual)

if __name__ == '__main__':
    unittest.main()

