from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        middle = len(s) // 2
        for i in range(middle):
            right = len(s) - 1 - i
            # swap the character
            temp = s[i]
            s[i] = s[right]
            s[right] = temp
            