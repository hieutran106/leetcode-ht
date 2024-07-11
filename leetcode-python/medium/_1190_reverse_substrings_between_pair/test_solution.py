import unittest
import collections
class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = [collections.deque()] # insert default queue
        for c in s:
            if c == '(':
                stack.append(collections.deque())
            elif c == ')':
                q = stack.pop()
                q.reverse()
                top = stack[-1]
                for char in q:
                    top.append(char)
            else:
                q = stack[-1]
                q.append(c)
        q = stack[0]
        l = list(q)
        ans = "".join(l)
        return ans

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.reverseParentheses("(abcd)")
        self.assertEqual(actual, "dcba")
        
    def test_case_2(self):
        actual = self.s.reverseParentheses("(u(love)i)")
        self.assertEqual(actual, "iloveu")

    def test_case_3(self):
        actual = self.s.reverseParentheses("(ed(et(oc))el)")
        self.assertEqual(actual, "leetcode")

    def test_case_4(self):
        actual = self.s.reverseParentheses("ab(cd)ef")
        self.assertEqual(actual, "abdcef")

    def test_case_5(self):
        actual = self.s.reverseParentheses("a(ed(et(oc))el)")
        self.assertEqual(actual, "aleetcode")

    def test_case_6(self):
        actual = self.s.reverseParentheses("abc")
        self.assertEqual(actual, "abc")

if __name__ == '__main__':
    unittest.main()

