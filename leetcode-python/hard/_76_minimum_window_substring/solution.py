from typing import List


def char_to_index(c: str):
    if c.islower():
        return ord(c) - ord('a')
    # upper case
    return ord(c) - ord('A') + 26


def contain(window: List[int], t: List[int]):
    for i in range(len(window)):
        if window[i] < t[i]:
            return False
    return True

def get_frequency(s: str):
    freq = [0] * 26 * 2
    for c in s:
        i = char_to_index(c)
        freq[i] += 1
    return freq

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window = get_frequency(s)
        T = get_frequency(t)
        left = 0
        right = len(s) - 1
        found = None
        while left < len(s):
            if contain(window, T):
                print(f"Found: {s[left:right+1]}")
                found = (left, right)
                # shrink the window
                right_char = s[right]
                window[char_to_index(right_char)] -= 1
                right -= 1
            else:
                left_char = s[left]
                window[char_to_index(left_char)] -= 1
                left += 1

                # move right pointer if there is enough room
                if right < len(s) - 1:
                    right += 1
                    right_char = s[right]
                    window[char_to_index(right_char)] += 1

        return s[found[0]: found[1] + 1] if found is not None else ""

