from typing import List


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        dict = {}
        for i in arr:
            value = dict.get(i, 0)
            dict[i] = value + 1

        result = - 1
        for key, value in dict.items():
            if key == value and key > result:
                result = key

        return result
