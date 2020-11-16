from typing import List

'''
Given a string S that only contains "I" (increase) or "D" (decrease), let N = S.length.

Return any permutation A of [0, 1, ..., N] such that for all i = 0, ..., N-1:

If S[i] == "I", then A[i] < A[i+1]
If S[i] == "D", then A[i] > A[i+1]
'''


class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        result = [i for i in range(len(S) + 1)]
        for i in range(len(result) - 1):
            for j in range(i + 1, len(result)):
                if S[i] == 'I' and result[i] < result[j]:
                    self.swap(result, i, j)
                elif S[i] == 'D' and result[i] > result[j]:
                    self.swap(result, i, j)

        return []

    def swap(self, array, i, j):
        temp = array[i]
        array[i] = array[j]
        array[j] = temp
