import unittest
from .solution import Solution


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def test_case1(self):
        words = ["This", "is", "an", "example", "of", "text", "justification."]
        maxWidth = 16
        actual = self.s.fullJustify(words, maxWidth)
        expected = ["This    is    an", "example  of text", "justification.  "]
        self.assertEqual(actual, expected)

    def test_case2(self):
        words = ["What", "must", "be", "acknowledgment", "shall", "be"]
        maxWidth = 16
        actual = self.s.fullJustify(words, maxWidth)
        expected = ["What   must   be", "acknowledgment  ", "shall be        "]
        self.assertEqual(actual, expected)

    def test_case3(self):
        words = [
            "Science",
            "is",
            "what",
            "we",
            "understand",
            "well",
            "enough",
            "to",
            "explain",
            "to",
            "a",
            "computer.",
            "Art",
            "is",
            "everything",
            "else",
            "we",
            "do",
        ]
        maxWidth = 20

        expected = [
            "Science  is  what we",
            "understand      well",
            "enough to explain to",
            "a  computer.  Art is",
            "everything  else  we",
            "do                  ",
        ]
        expected_badness = sum(map(lambda x: x.count(' '), expected))

        words_lens = list(map(lambda x: len(x), words))
        memo = {}
        break_points = [None for i in range(len(words))]
        actual_min_badness = self.s.findMinBadness(words, words_lens, maxWidth, 0, memo, break_points)
        # self.assertEqual(actual_min_badness, expected_badness)

        actual = self.s.fullJustify(words, maxWidth)
        print(actual)
        self.assertEqual(actual, expected)

    def test_case4(self):
        words = [
            "Don't",
            "go",
            "around",
            "saying",
            "the",
            "world",
            "owes",
            "you",
            "a",
            "living;",
            "the",
            "world",
            "owes",
            "you",
            "nothing;",
            "it",
            "was",
            "here",
            "first.",
        ]
        maxWidth = 30
        actual = self.s.fullJustify(words, maxWidth)
        expected = [
            "Don't  go  around  saying  the", # 8
            "world  owes  you a living; the", # 7
            "world owes you nothing; it was", # 5
            "here first.                   ", # 20
        ]
        self.assertEqual(actual, expected)

    def test_findMinBadness1(self):
        words = ["aaaa", "a"]
        maxWidth = 10
        words_lens = list(map(lambda x: len(x), words))
        memo = {}
        break_points = [None for i in range(len(words))]
        actual = self.s.findMinBadness(words, words_lens, maxWidth, len(words) - 1, memo, break_points)

        self.assertEqual(actual, 5)

    def test_findMinBadness2(self):
        words = ["aaaa", "a", "aaaaaaaa"]
        maxWidth = 10
        words_lens = list(map(lambda x: len(x), words))
        memo = {}
        break_points = [None for i in range(len(words))]
        actual = self.s.findMinBadness(words, words_lens, maxWidth, len(words) -1, memo, break_points)

        expected = [
            'aaaa     a',
            'aaaaaaaa  '
        ]
        expected_badness = sum(map(lambda x: x.count(' '), expected))
        self.assertEqual(actual, expected_badness)

    # def test_findMinBadness3(self):
    #     words = [
    #         "Don't",
    #         "go",
    #         "around",
    #         "saying",
    #         "the",
    #         "world",
    #         "owes",
    #         "you",
    #         "a",
    #         "living;",
    #         "the",
    #         "world",
    #         "owes",
    #         "you",
    #         "nothing;",
    #         "it",
    #         "was",
    #         "here",
    #         "first.",
    #     ]
    #     maxWidth = 30
    #     words_lens = list(map(lambda x: len(x), words))
    #     memo = {}
    #     actual = self.s.findMinBadness(words, words_lens, maxWidth, 0, memo)
    #     expected = [
    #         "Don't  go  around  saying  the",  # 8
    #         "world  owes  you a living; the",  # 7
    #         "world owes you nothing; it was",  # 5
    #         "here first.                   ",  # 20
    #     ]
    #     expected_badness = sum(map(lambda x: x.count(' '), expected))
    #     self.assertEqual(actual, expected_badness)
    #
    # def test_findMinBadness4(self):
    #     words = ["This", "is", "an", "example", "of", "text", "justification."]
    #     maxWidth = 16
    #     words_lens = list(map(lambda x: len(x), words))
    #     memo = {}
    #
    #     actual = self.s.findMinBadness(words, words_lens, maxWidth, 0, memo)
    #     expected = ["This    is    an", "example  of text", "justification.  "]
    #     expected_badness = sum(map(lambda x: x.count(' '), expected))
    #     self.assertEqual(actual, expected_badness)


if __name__ == "__main__":
    unittest.main()
