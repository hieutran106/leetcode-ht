import unittest
from typing import List, Dict, Set


# Date: 2025-10-09
# Problem: 1733 min_people_to_teach
class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        lang_map: Dict[int, Set] = {}
        for i, lan_arr in enumerate(languages):
            lang_map[i + 1] = set(lan_arr)
        needToTeach = set()
        for u, v in friendships:
            if lang_map[u].intersection(lang_map[v]):
                continue
            needToTeach.add(u)
            needToTeach.add(v)

        ans = float("inf")
        for l in range(1, n + 1):
            user_count = 0
            for u in needToTeach:
                if l not in lang_map[u]:
                    user_count += 1
            ans = min(ans, user_count)

        return ans


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        actual = self.s.minimumTeachings(n=2, languages=[[1], [2], [1, 2]], friendships=[[1, 2], [1, 3], [2, 3]])
        self.assertEqual(1, actual)

    def test_case_2(self):
        actual = self.s.minimumTeachings(n=3, languages=[[2], [1, 3], [1, 2], [3]],
                                         friendships=[[1, 4], [1, 2], [3, 4], [2, 3]])
        self.assertEqual(2, actual)

    def test_case_3(self):
        actual = self.s.minimumTeachings(n=2, languages=[[1], [1, 2]], friendships=[[1, 2]])
        self.assertEqual(0, actual)

    def test_case_4(self):
        actual = (self.s.
                  minimumTeachings(n=11,
                                   languages=[[3, 11, 5, 10, 1, 4, 9, 7, 2, 8, 6], [5, 10, 6, 4, 8, 7], [6, 11, 7, 9],
                                              [11, 10, 4], [6, 2, 8, 4, 3], [9, 2, 8, 4, 6, 1, 5, 7, 3, 10],
                                              [7, 5, 11, 1, 3, 4], [3, 4, 11, 10, 6, 2, 1, 7, 5, 8, 9],
                                              [8, 6, 10, 2, 3, 1, 11, 5], [5, 11, 6, 4, 2]],
                                   friendships=[[7, 9], [3, 7], [3, 4], [2, 9], [1, 8], [5, 9], [8, 9], [6, 9], [3, 5],
                                                [4, 5], [4, 9], [3, 6], [1, 7], [1, 3], [2, 8], [2, 6], [5, 7], [4, 6],
                                                [5, 8], [5, 6], [2, 7], [4, 8], [3, 8], [6, 8], [2, 5], [1, 4], [1, 9],
                                                [1, 6], [6, 7]]))
        self.assertEqual(0, actual)

    def test_case_5(self):
        actual = (self.s.
                  minimumTeachings(n=17,
                                   languages=[[4, 7, 2, 14, 6], [15, 13, 6, 3, 2, 7, 10, 8, 12, 4, 9], [16], [10],
                                              [10, 3], [4, 12, 8, 1, 16, 5, 15, 17, 13],
                                              [4, 13, 15, 8, 17, 3, 6, 14, 5, 10],
                                              [11, 4, 13, 8, 3, 14, 5, 7, 15, 6, 9, 17, 2, 16, 12], [4, 14, 6],
                                              [16, 17, 9, 3, 11, 14, 10, 12, 1, 8, 13, 4, 5, 6], [14], [7, 14],
                                              [17, 15, 10, 3, 2, 12, 16, 14, 1, 7, 9, 6, 4]],
                                   friendships=[[4, 11], [3, 5], [7, 10], [10, 12], [5, 7], [4, 5], [3, 8], [1, 5],
                                                [1, 6], [7, 8], [4, 12], [2, 4], [8, 9], [3, 10], [4, 7], [5, 12],
                                                [4, 9], [1, 4], [2, 8], [1, 2], [3, 4], [5, 10], [2, 7], [1, 7], [1, 8],
                                                [8, 10], [1, 9], [1, 10], [6, 7], [3, 7], [8, 12], [7, 9], [9, 11],
                                                [2, 5], [2, 3]]))
        self.assertEqual(4, actual)


if __name__ == '__main__':
    unittest.main()
