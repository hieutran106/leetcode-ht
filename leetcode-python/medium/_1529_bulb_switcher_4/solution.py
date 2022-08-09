'''
Choose a bulb i, then flip each bulb from index i to n-1. That means, the 0-th bulb can only be flipped by choosing itself. And then, choosing any bulb else will not change bulb 0.
Flip even times -> bulb unchanged. Flip odd times -> bulb changed to 1.
Iterate from 0 to N - 1. Greedily flip the bulb if it is unmatched with target (But, you need to check how many times it has been flipped).
'''
class Solution:
    def minFlips(self, target: str) -> int:
        num_flip = 0

        for c in target:
            if (num_flip %2 ==0 and c == '1') or (num_flip %2 == 1 and c == '0'):
                num_flip += 1

        return num_flip







