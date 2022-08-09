class Solution:
    """
    s[c] is always an answer
    check surrounding in which s[c] is the central, for example 'abc'
    check surrounding in which s[c] is on the left, for example 'aa'
    """
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        total = 0
        for c, i in enumerate(s):
            j = 1
            total += 1 # s[c] is always an answer
            # check surrounding in which s[c] is the central, for example 'abc'
            while c-j >=0 and c+j < n:
                if s[c-j] == s[c+j]:
                    total += 1
                    j += 1
                else:
                    break
            # check surrounding in which s[c] is on the left, for example 'aa'
            j = 0
            while c -j -1 >=0 and c+j < n:
                if s[c-j-1] == s[c+j]:
                    total += 1
                    j += 1
                else:
                    break
        return total
