class Solution:
    def findTheDifference(self, s: str, t: str) -> str:

        result = [0 for i in range(26)]
        ascii_a = ord('a')
        for i in range(len(s)):
            c_s = s[i]
            c_t = t[i]
            result[ord(c_s) - ascii_a] += 1
            result[ord(c_t) - ascii_a] -= 1

        result[ord(t[-1]) - ascii_a] -= 1


        # find the element with occurence 1
        for i in range(len(result)):
            if result[i] == -1:
                return chr(i + ascii_a)

        return None

