from typing import List

'''
Given a string S that only contains "I" (increase) or "D" (decrease), let N = S.length.

Return any permutation A of [0, 1, ..., N] such that for all i = 0, ..., N-1:

If S[i] == "I", then A[i] < A[i+1]
If S[i] == "D", then A[i] > A[i+1]
'''

class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        i = 0
        j = len(S)
        ans = []

        for c in S:
            if c == 'I':
                ans.append(i)
                i += 1
            else:
                ans.append(j)
                j -= 1

        # latest element
        ans.append(j)
        return ans
