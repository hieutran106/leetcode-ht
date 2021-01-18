# tags: math, permutation, repetition
import collections
import functools
import itertools

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        occurrence = list(collections.Counter(tiles).values())
        result = 0
        loop = [[i for i in range(v+1)] for v in occurrence]
        factorial = [1, 1, 2, 6, 24, 120, 720, 5040]
        cache = {}
        for nums in itertools.product(*loop):
            if sum(nums) == 0:
                continue
            result += self.calculate(nums, factorial, cache)

        return result

    def calculate(self, nums, factorial, cache):
        key = tuple(sorted(nums))
        if key not in cache:
            numerator = factorial[sum(nums)]
            denominator = functools.reduce(lambda acc, ele: acc * factorial[ele], nums, 1)
            result = numerator // denominator
            cache[key] = result

        return cache[key]




