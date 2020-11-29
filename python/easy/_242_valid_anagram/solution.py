class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        result = [0 for i in range(26)]
        for i in range(len(s)):
            c_s = s[i]
            c_t = t[i]
            result[ord(c_s) - ord('a')] += 1
            result[ord(c_t) - ord('a')] -= 1

        # check all element in result is zero
        result = all(e ==0 for e in result)
        return result


class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dict = {}
        for i in range(len(s)):
            c_s = s[i]
            c_t = t[i]
            val1 = dict.get(c_s, 0)
            dict[c_s] = val1 + 1

            val2 = dict.get(c_t, 0)
            dict[c_t] = val2 - 1

        for v in dict.values():
            if v != 0:
                return False

        return True


