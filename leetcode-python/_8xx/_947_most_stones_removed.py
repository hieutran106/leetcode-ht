import unittest
from typing import List


class UnionFind:
    def __init__(self, stones: List[List[int]]):
        self.parent = {}
        self.internals = {} # the number of elements in each set
        for x, y in stones:
            self.parent[(x, y)] = (x, y)
            self.internals[(x, y)] = 1

    def find_root(self, x):
        if self.parent[x] != x:
            return self.find_root(self.parent[x])
        return x

    def union(self, p1, p2):
        root_p1 = self.find_root(p1)
        root_p2 = self.find_root(p2)

        if root_p1 != root_p2:
            self.parent[root_p2] = root_p1

            self.internals[root_p1] += self.internals[root_p2]
            del self.internals[root_p2]


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        union_find = UnionFind(stones)
        for i in range(0, len(stones) - 1):
            for j in range(i + 1, len(stones)):
                x1, y1 = stones[i]
                x2, y2 = stones[j]
                if x1 == x2 or y1 == y2:
                    p1 = (x1, y1)
                    p2 = (x2, y2)
                    union_find.union(p1, p2)
        # print(union_find.internals)
        ans = 0
        for size in union_find.internals.values():
            if size > 1:
                ans += size - 1
        return ans


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        actual = self.s.removeStones(stones=[[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]])
        self.assertEqual(5, actual)

    def test_case_2(self):
        actual = self.s.removeStones(stones=[[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]])
        self.assertEqual(3, actual)

    def test_case_3(self):
        actual = self.s.removeStones(stones=[[0, 0]])
        self.assertEqual(0, actual)


if __name__ == '__main__':
    unittest.main()
