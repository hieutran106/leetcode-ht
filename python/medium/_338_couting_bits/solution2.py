'''
If the number(n) is even then the count of set bits in number will be same as count of set bits in n/2

If the number (n) is odd then the count of set bits in number will be same as count of set bits in n/2+1
'''
from typing import List


class Solution2:
    def countBits(self, num: int) -> List[int]:
        result = [0] * (num + 1)
        for i in range(1, num + 1):
            if i % 2 == 0:
                result[i] = result[i // 2]
            else:
                result[i] = result[i // 2] + 1

        return result
