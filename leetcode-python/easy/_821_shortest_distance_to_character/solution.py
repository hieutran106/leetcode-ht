from typing import List
import math

class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        positions = []
        for idx, c in enumerate(S):
            if c == C:
                positions.append(idx)

        result = []
        for idx, c in enumerate(S):
            if c == C:
                result.append(0)
            else:
                min_distance = min(map(lambda pos: abs(pos - idx), positions))
                result.append(min_distance)

        return result
