import unittest
from typing import List

class Solution:
    def smallestNumber(self, pattern: str) -> str:
        """
        backtrack and greedy
        """
        visit = set()
        path = []

        def backtrack(path: List[int], j):
            if j == len(pattern) + 1:
                return "".join(map(str, path))
            for num in range(1, 10):
                if num in visit:
                    continue
                if j == 0 or (pattern[j-1] == 'I' and num > path[-1]) or (pattern[j-1] == 'D' and num < path[-1]):
                    path.append(num)
                    visit.add(num)
                    ans = backtrack(path, j + 1)
                    if ans:
                        return ans
                    visit.remove(num)
                    path.pop()

        ans = backtrack(path, 0)
        return ans


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.smallestNumber(pattern = "IIIDIDDD")
        self.assertEqual(actual, "123549876")
        
    def test_case_2(self):
        actual = self.s.smallestNumber(pattern="DDD")
        self.assertEqual(actual, "4321")

    def test_case_3(self):
        actual = self.s.smallestNumber(pattern="DDDI")
        self.assertEqual(actual, "43215")

    def test_case_4(self):
        actual = self.s.smallestNumber(pattern="I")
        self.assertEqual(actual, "12")

    def test_case_5(self):
        actual = self.s.smallestNumber(pattern="D")
        self.assertEqual(actual, "21")

if __name__ == '__main__':
    unittest.main()

