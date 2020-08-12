
'''
    Bit count solution
        Count each 0 as 1.
        Count each 1 as 2 except the first 1.
'''
class Solution2:
    def numberOfSteps (self, num: int) -> int:
        digits = f'{num:b}'
        return digits.count('1') - 1 + len(digits)