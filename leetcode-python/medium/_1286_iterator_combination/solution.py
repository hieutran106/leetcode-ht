from typing import List


class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.characters = characters
        self.combinationLength = combinationLength
        self.combi = self.combine(characters, combinationLength)

    def combine(self, characters: str, combinationLength: int) -> List[int]:
        result = []
        path = []
        self.backtrack(path, 0, combinationLength, characters, result)
        return result

    def backtrack(self, path: List[str], start: int, combinationLength: int, characters: str,
                  result: List[str]) -> None:
        if len(path) == combinationLength:
            result.append("".join(path))
            return

        for i in range(start, len(characters)):
            path.append(characters[i])
            self.backtrack(path, i + 1, combinationLength, characters, result)
            path.pop()

    def next(self) -> str:
        return self.combi.pop(0)


    def hasNext(self) -> bool:
        return len(self.combi) > 0
