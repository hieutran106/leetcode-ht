import unittest
from typing import List, Set
import  collections

from Tools.scripts.md5sum import usage


#2025-03-04
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        d = {} # last index of character
        stack = [] # increasing monotonic stack
        for i, c in enumerate(s):
            d[c] = i
        for i, c in enumerate(s):
            print(f"start================== char={c}")
            if c in stack:
                continue
            while stack and ord(stack[-1]) > ord(c) and d[stack[-1]] > i:
                print(f"Pop {stack[-1]}")
                stack.pop()

            stack.append(c)
            print(f"end========")

        print(stack)
        return "".join(stack)

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.removeDuplicateLetters(s = "bcabc")
        self.assertEqual("abc", actual)
        
    def test_case_2(self):
        actual = self.s.removeDuplicateLetters(s="cbacdcbc")
        self.assertEqual("acdb", actual)

    def test_case_3(self):
        actual = self.s.removeDuplicateLetters(s="zyxyabz")
        self.assertEqual("xyabz", actual)

    def test_case_4(self):
        actual = self.s.removeDuplicateLetters(s="bdacbbcd")
        self.assertEqual("abcd", actual)

    def test_case_5(self):
        actual = self.s.removeDuplicateLetters(s="cdadabcc")
        self.assertEqual("adbc", actual)

    def test_case_6(self):
        actual = self.s.removeDuplicateLetters(s="abacb")
        self.assertEqual("abc", actual)

if __name__ == '__main__':
    unittest.main()

