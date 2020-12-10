# tags: dp

from typing import List

class Solution:
    '''
    The idea is the following:

    d is an array that contains booleans

    d[i] is True if there is a word in the dictionary that ends at ith index of s AND d is also True at the beginning of the word

    Example:

    s = "leetcode"

    words = ["leet", "code"]

    d[3] is True because there is "leet" in the dictionary that ends at 3rd index of "leetcode"

    d[7] is True because there is "code" in the dictionary that ends at the 7th index of "leetcode" AND d[3] is True
    '''
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False for i in range(n+1)]

        dp[0] = True
        for i in range(1, n+1):
            for w in wordDict:
                if dp[i - len(w)] and s[i - len(w): i] == w:
                    dp[i] = True
                    break

        return dp[-1]



