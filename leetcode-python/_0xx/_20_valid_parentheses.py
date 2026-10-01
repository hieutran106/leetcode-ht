import unittest
from typing import List

# Date: 2026-10-01
# Problem: 20 valid_parentheses
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
                continue
            if len(stack) == 0:
                return False
            if c== ')' and stack[-1] == '(':
                stack.pop()
            elif c == ']' and stack[-1] == '[':
                stack.pop()
            elif c == '}' and stack[-1] == '{':
                stack.pop()
            else:
                return False

        return len(stack) == 0
    

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.isValid(s = "()")
        self.assertEqual(True, actual)
        
    def test_case_2(self):
        actual = self.s.isValid(s="()[]{}")
        self.assertEqual(True, actual)

    def test_case_3(self):
        actual = self.s.isValid(s = "(]")
        self.assertEqual(False, actual)

    def test_case_4(self):
        actual = self.s.isValid(s = "([])")
        self.assertEqual(True, actual)

    def test_case_5(self):
        actual = self.s.isValid(s = "([)]")
        self.assertEqual(False, actual)

if __name__ == '__main__':
    unittest.main()

