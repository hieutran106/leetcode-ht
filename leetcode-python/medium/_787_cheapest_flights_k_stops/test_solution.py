import collections
import unittest
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        def build_graph(flights):
            res = collections.defaultdict(list)
            for flight in flights:
                source, destination, price = flight
                # Entry (price, destination)
                res[source].append((price, destination))
            return res

        # graph represented as a dictionary of list (price, destination)
        graph = build_graph(flights)
        distances = {node: float("infinity") for node in range(n)}
        q = collections.deque([(0, src)]) # (price, node)
        stop_count = 0
        while q and stop_count <= k:
            length = len(q)
            for i in range(length):
                curr_price, node = q.popleft()
                if node not in graph:
                    continue
                for price, neighbor in graph[node]:
                    next_price = curr_price + price
                    if next_price >= distances[neighbor]:
                        continue
                    distances[neighbor] = next_price
                    q.append((next_price, neighbor))
            stop_count += 1
        return distances[dst] if distances[dst] != float("infinity") else -1


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        actual = self.s.findCheapestPrice(n=4,
                                          flights=[[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]],
                                          src=0, dst=3, k=1)
        self.assertEqual(actual, 700)

    def test_case_2(self):
        actual = self.s.findCheapestPrice(n=3, flights=[[0, 1, 100], [1, 2, 100], [0, 2, 500]], src=0, dst=2, k=1)
        self.assertEqual(actual, 200)

    def test_case_3(self):
        actual = self.s.findCheapestPrice(n=3, flights=[[0, 1, 100], [1, 2, 100], [0, 2, 500]], src=0, dst=2, k=0)
        self.assertEqual(actual, 500)

    def test_case_4(self):
        actual = self.s.findCheapestPrice(n=3, flights=[[0, 1, 100], [1, 2, 100]], src=0, dst=2, k=0)
        self.assertEqual(actual, -1)

    def test_case_5(self):
        actual = self.s.findCheapestPrice(n=13, flights=[[11, 12, 74], [1, 8, 91], [4, 6, 13], [7, 6, 39], [5, 12, 8],
                                                         [0, 12, 54], [8, 4, 32], [0, 11, 4], [4, 0, 91], [11, 7, 64],
                                                         [6, 3, 88], [8, 5, 80], [11, 10, 91], [10, 0, 60], [8, 7, 92],
                                                         [12, 6, 78], [6, 2, 8], [4, 3, 54], [3, 11, 76], [3, 12, 23],
                                                         [11, 6, 79], [6, 12, 36], [2, 11, 100], [2, 5, 49], [7, 0, 17],
                                                         [5, 8, 95], [3, 9, 98], [8, 10, 61], [2, 12, 38], [5, 7, 58],
                                                         [9, 4, 37], [8, 6, 79], [9, 0, 1], [2, 3, 12], [7, 10, 7],
                                                         [12, 10, 52], [7, 2, 68], [12, 2, 100], [6, 9, 53], [7, 4, 90],
                                                         [0, 5, 43], [11, 2, 52], [11, 8, 50], [12, 4, 38], [7, 9, 94],
                                                         [2, 7, 38], [3, 7, 88], [9, 12, 20], [12, 0, 26], [10, 5, 38],
                                                         [12, 8, 50], [0, 2, 77], [11, 0, 13], [9, 10, 76], [2, 6, 67],
                                                         [5, 6, 34], [9, 7, 62], [5, 3, 67]], src=10, dst=1, k=10)
        self.assertEqual(actual, -1)

    def test_case_7(self):
        actual = self.s.findCheapestPrice(n=10,
                                          flights=[[3, 4, 4], [2, 5, 6], [4, 7, 10], [9, 6, 5], [7, 4, 4], [6, 2, 10],
                                                   [6, 8, 6], [7, 9, 4], [1, 5, 4], [1, 0, 4], [9, 7, 3], [7, 0, 5],
                                                   [6, 5, 8], [1, 7, 6], [4, 0, 9], [5, 9, 1], [8, 7, 3], [1, 2, 6],
                                                   [4, 1, 5], [5, 2, 4], [1, 9, 1], [7, 8, 10], [0, 4, 2], [7, 2, 8]],
                                          src=6, dst=0, k=7)
        self.assertEqual(actual, 14)

    def test_case_8(self):
        actual = self.s.findCheapestPrice(n=13,
                                          flights=[[11, 12, 74], [1, 8, 91], [4, 6, 13], [7, 6, 39], [5, 12, 8],
                                                   [0, 12, 54], [8, 4, 32], [0, 11, 4], [4, 0, 91], [11, 7, 64],
                                                   [6, 3, 88], [8, 5, 80], [11, 10, 91], [10, 0, 60], [8, 7, 92],
                                                   [12, 6, 78], [6, 2, 8], [4, 3, 54], [3, 11, 76], [3, 12, 23],
                                                   [11, 6, 79], [6, 12, 36], [2, 11, 100], [2, 5, 49], [7, 0, 17],
                                                   [5, 8, 95], [3, 9, 98], [8, 10, 61], [2, 12, 38], [5, 7, 58],
                                                   [9, 4, 37], [8, 6, 79], [9, 0, 1], [2, 3, 12], [7, 10, 7],
                                                   [12, 10, 52], [7, 2, 68], [12, 2, 100], [6, 9, 53], [7, 4, 90],
                                                   [0, 5, 43], [11, 2, 52], [11, 8, 50], [12, 4, 38], [7, 9, 94],
                                                   [2, 7, 38], [3, 7, 88], [9, 12, 20], [12, 0, 26], [10, 5, 38],
                                                   [12, 8, 50], [0, 2, 77], [11, 0, 13], [9, 10, 76], [2, 6, 67],
                                                   [5, 6, 34], [9, 7, 62], [5, 3, 67]],
                                          src=10, dst=1, k=10)
        self.assertEqual(actual, -1)

    def test_case_9(self):
        actual = self.s.findCheapestPrice(n=11,
                                          flights=[[0, 3, 3], [3, 4, 3], [4, 1, 3], [0, 5, 1], [5, 1, 100], [0, 6, 2],
                                                   [6, 1, 100], [0, 7, 1], [7, 8, 1], [8, 9, 1], [9, 1, 1], [1, 10, 1],
                                                   [10, 2, 1], [1, 2, 100]], src=0, dst=2, k=4)
        self.assertEqual(actual, 11)


if __name__ == '__main__':
    unittest.main()
