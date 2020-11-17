from typing import List
from math import log, ceil

class Solution:
    def countBits(self, num: int) -> List[int]:
        bit = ceil(log(num+1, 2))
        representation = [0] * bit
        result = [0] * (num + 1)

        for i in range(1, num + 1):
            self.increase_one(representation)
            result[i] = representation.count(1)

        return result

    def increase_one(self, representation):
        for i in reversed(range(len(representation))):
            if representation[i] == 0:
                representation[i] = 1
                break
            else:
                representation[i] = 0
