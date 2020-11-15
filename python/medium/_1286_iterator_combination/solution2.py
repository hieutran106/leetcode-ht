
class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.characters = characters
        self.len = combinationLength

        if len(characters) < combinationLength:
            self.has_next_item = False
        else:
            self.has_next_item = True

        # use an array to store indexes of characters in a combination
        self.stack_call = []
        for i in range(combinationLength):
            self.stack_call.append(i)

    def set(self, stack_call, has_next_item):
        self.stack_call = stack_call
        self.has_next_item = has_next_item

    def next(self) -> str:
        result = "".join(map(lambda index: self.characters[index], self.stack_call))
        # prepare for next iteration

        top = self.stack_call.pop()
        while len(self.stack_call) < self.len:
            # index of candidate in the string
            candidate = top + 1
            if self.has_valid_candidate(candidate):
                # push the candidate index to the top of stack
                self.stack_call.append(candidate)
                top = candidate
                continue

            if len(self.stack_call) == 0:
                self.has_next_item = False
                break
            else:
                top = self.stack_call.pop()

        # check if we can generate another combination
        return result

    def has_valid_candidate(self, candidate):
        return candidate + self.len - len(self.stack_call) <= len(self.characters)

    def hasNext(self) -> bool:
        return self.has_next_item


class DataAnalyzer:
    train_data: int
    test_data: int

    def __init__(self, train_data: int, test_data: str):
        self.train_data = train_data
        self.test_data = test_data
