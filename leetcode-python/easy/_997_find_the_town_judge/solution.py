from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        village_trusts = [0 for _ in range(n)]
        trustee = [0 for _ in range(n)]
        for t in trust:
            a = t[0]
            b = t[1]
            village_trusts[b-1] += 1
            trustee[a-1] += 1

        for index, count in enumerate(village_trusts):
            if count == n - 1 and trustee[index] == 0:
                return index + 1
        return -1