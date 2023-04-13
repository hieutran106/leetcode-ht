from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(i: int, curr: List[int], total: int):
            if total == target:
                res.append(curr.copy())
                return
            elif total > target or i >= len(candidates):
                return

            # include number at i-th
            curr.append(candidates[i])
            backtrack(i, curr, total + candidates[i])
            # NOT include number at i-th
            curr.pop()
            backtrack(i+1, curr, total)

        backtrack(0, [], 0)
        return res
