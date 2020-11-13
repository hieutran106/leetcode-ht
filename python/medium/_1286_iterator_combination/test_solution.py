import unittest
from typing import List

from .solution2 import CombinationIterator


def combine(characters: str, combinationLength: int) -> List[int]:
    result = []
    path = []
    backtrack(path, 0, combinationLength, characters, result)
    return result


def backtrack(path: List[str], start: int, combinationLength: int, characters: str,
              result: List[str]) -> None:
    if len(path) == combinationLength:
        result.append("".join(path))
        return

    for i in range(start, len(characters)):
        path.append(characters[i])
        backtrack(path, i + 1, combinationLength, characters, result)
        path.pop()


class MyTestCase(unittest.TestCase):

    def test_something(self):
        iterator = CombinationIterator("abc", 2)
        next = iterator.next()

        self.assertEqual("ab", next)
        self.assertEqual(True, iterator.hasNext())

        self.assertEqual("ac", iterator.next())
        self.assertEqual(True, iterator.hasNext())

        self.assertEqual("bc", iterator.next())
        self.assertEqual(False, iterator.hasNext())

    def test_case_2(self):
        iterator = CombinationIterator("abc", 2)
        iterator.set([1, 2], True)

        # assert
        next = iterator.next()
        self.assertEqual(next, "bc")
        has_next = iterator.hasNext()
        self.assertEqual(has_next, False)

    def test_case_3(self):
        iterator = CombinationIterator("abcde", 3)
        iterator.set([0, 3, 4], True)

        # assert
        next = iterator.next()
        self.assertEqual(next, "ade")
        self.assertCountEqual(iterator.stack_call, [1, 2, 3])

    def test_case_4(self):
        iterator = CombinationIterator("abcde", 3)
        iterator.set([1, 2, 3], True)

        # assert
        next = iterator.next()
        self.assertEqual(next, "bcd")
        self.assertCountEqual(iterator.stack_call, [1, 2, 4])

    def test_case_5(self):
        iterator = CombinationIterator("abcde", 3)
        iterator.set([2, 3, 4], True)

        # assert
        next = iterator.next()
        self.assertEqual(next, "cde")

    def test_case_6(self):
        iterator = CombinationIterator("abcd", 3)
        result = []
        while (iterator.hasNext()):
            result.append(iterator.next())

        expect = combine("abcd", 3)
        self.assertCountEqual(expect, result)

    def test_case_7(self):
        iterator = CombinationIterator("abcdefgh", 4)
        result = []
        while (iterator.hasNext()):
            result.append(iterator.next())

        expect = combine("abcdefgh", 4)
        self.assertCountEqual(expect, result)

    def test_case_7(self):
        iterator = CombinationIterator("", 1)
        result = []
        while (iterator.hasNext()):
            result.append(iterator.next())


        self.assertCountEqual([], result)

if __name__ == '__main__':
    unittest.main()
