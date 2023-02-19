import unittest
from .solution import Solution


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        actual = self.s.ladderLength(beginWord="hit", endWord="cog",
                                     wordList=["hot", "dot", "dog", "lot", "log", "cog"])
        self.assertEqual(5, actual)

    def test_case_2(self):
        actual = self.s.ladderLength(beginWord="hit", endWord="cog", wordList=["hot", "dot", "dog", "lot", "log"])
        self.assertEqual(0, actual)

    def test_case_3(self):
        actual = self.s.ladderLength(beginWord="hit", endWord="cog",
                                     wordList=["hot", "cog", "dot", "dog", "hit", "lot", "log"])
        self.assertEqual(5, actual)


if __name__ == '__main__':
    unittest.main()
