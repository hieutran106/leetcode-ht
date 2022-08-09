from typing import List

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        dict = {}
        for pairs in paths:
            dict[pairs[0]] = pairs[1]

        start = paths[0][0]
        while start in dict:
            start = dict[start]

        return start

