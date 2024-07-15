import unittest
from typing import List


class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        indexes = [i for i in range(len(positions))]
        zipped = list(zip(positions, healths, directions, indexes))
        zipped.sort(key=lambda x: x[0])
        stack = []
        for pos, heath, dir, i in zipped:
            if not stack:
                stack.append([heath, dir, i])
                continue
            prev = stack[-1]
            if prev[1] != 'R' or dir != 'L':
                # not collision
                stack.append([heath, dir, i])
                continue
            # collision
            should_push = False
            while prev and prev[1] == 'R' and dir == 'L':
                if prev[0] == heath:
                    should_push = False
                    stack.pop()
                    break
                if prev[0] > heath:
                    should_push = False
                    prev[0] -= 1
                    break
                stack.pop()
                heath -= 1
                should_push = True
                if stack:
                    prev = stack[-1]
                else:
                    prev = None
            if should_push:
                stack.append([heath, dir, i])
        stack.sort(key=lambda x: x[2])
        ans = []
        for ele in stack:
            ans.append(ele[0])
        return ans


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        actual = self.s.survivedRobotsHealths(positions=[5, 4, 3, 2, 1], healths=[2, 17, 9, 15, 10], directions="RRRRR")
        self.assertEqual(actual, [2, 17, 9, 15, 10])

    def test_case_2(self):
        actual = self.s.survivedRobotsHealths(positions=[3, 5, 2, 6], healths=[10, 10, 15, 12], directions="RLRL")
        self.assertEqual(actual, [14])

    def test_case_3(self):
        actual = self.s.survivedRobotsHealths(positions=[1, 2, 5, 6], healths=[10, 10, 11, 11], directions="RLRL")
        self.assertEqual(actual, [])

    def test_case_4(self):
        actual = self.s.survivedRobotsHealths(positions=[3, 47], healths=[46, 26], directions="LR")
        self.assertEqual(actual, [46, 26])

    def test_case_5(self):
        actual = self.s.survivedRobotsHealths(positions=[11, 44, 16], healths=[1, 20, 17], directions="RLR")
        self.assertEqual(actual, [18])

    def test_case_6(self):
        actual = self.s.survivedRobotsHealths(positions=[34, 50, 42, 2], healths=[6, 27, 17, 38], directions="LLRR")
        self.assertEqual(actual, [36])


if __name__ == '__main__':
    unittest.main()
