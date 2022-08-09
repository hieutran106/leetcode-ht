import collections

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Permutation ==> use frequency to check
        Consider a substring start from a particular position
        Check frequency of potential and that of s1
        """
        s1_freq = collections.Counter(s1)
        for i in range(0, len(s2) - len(s1) + 1):
            curr = s2[i]
            if curr not in s1_freq:
                continue
            potential = collections.Counter(s2[i: i + len(s1)])
            if potential == s1_freq:
                return True
        return False

class Solution2:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        For each window representing a substring of s2 of length s1
        Compare metric of window to the frequency of char in s1
        """
        s1_freq = [0] * 26
        window = [0] * 26
        offset = ord('a')
        for c in s1:
            s1_freq[ord(c) - offset] += 1

        for i, c in enumerate(s2):
            window[ord(c) - offset] += 1
            if i >= len(s1):
                to_be_removed = s2[i - len(s1)]
                window[ord(to_be_removed) - offset] -= 1
            if window == s1_freq:
                return True
        return False