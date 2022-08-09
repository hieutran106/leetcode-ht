from typing import List
import sys

def wordBreak(s: str, wordDict: List[str]) -> bool:
    n = len(s)
    dp = [False for i in range(n + 1)]

    dp[0] = True
    for i in range(1, n + 1):
        for w in wordDict:
            if dp[i - len(w)] and s[i - len(w): i] == w:
                dp[i] = True
                break

    return dp[-1]


if __name__ == "__main__":
    my_input = [line.rstrip() for line in sys.stdin.readlines()]
#     my_input = """1 1 4
# 1 3 2"""
#     my_input = my_input.split("\n")
#     my_input = my_input[1:]
    word = my_input[0]
    wordDict = my_input[2:]
    print(word)
    print(wordDict)
    result = wordBreak(word, wordDict)
    print(result)


