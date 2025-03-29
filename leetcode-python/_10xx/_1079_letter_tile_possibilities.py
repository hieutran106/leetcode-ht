import unittest
from typing import List


class Solution1:
    """
    Use a set to store all possibilities
    """
    def numTilePossibilities(self, tiles: str) -> int:
        ans = set()

        def backtrack(path: List[str], candidates: str):
            if path:
                ans.add(''.join(path))
            if len(candidates) == 0:
                return
            for i in range(len(candidates)):
                path.append(candidates[i])
                backtrack(path, candidates[0:i] + candidates[i + 1:])
                path.pop()

        backtrack([], tiles)
        return len(ans)

class Solution:
    """
    Optimize by just count the possibilities
    """
    def numTilePossibilities(self, tiles: str) -> int:
        freq = [0] * 26
        for c in tiles:
            freq[ord(c) - ord('A')] += 1

        ans = 0
        def dfs(freq: List[int]):
            nonlocal ans
            for i in range(26):
                if freq[i] > 0:
                    freq[i] -= 1
                    ans += 1
                    dfs(freq)
                    freq[i] += 1
        dfs(freq)
        return ans

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        actual = self.s.numTilePossibilities(tiles="AAB")
        self.assertEqual(8, actual)

    def test_case_2(self):
        actual = self.s.numTilePossibilities(tiles="AAABBC")
        self.assertEqual(188, actual)

    def test_case_3(self):
        actual = self.s.numTilePossibilities(tiles="V")
        self.assertEqual(1, actual)

    def test_case_4(self):
        actual = self.s.numTilePossibilities(tiles="AA")
        self.assertEqual(2, actual)


if __name__ == '__main__':
    unittest.main()
