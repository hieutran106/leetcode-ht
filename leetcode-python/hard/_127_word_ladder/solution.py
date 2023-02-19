import collections
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord not in wordList:
            wordList.append(beginWord)

        adjacency_list = collections.defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[0:i] + "*" + word[i + 1:]
                adjacency_list[pattern].append(word)

        visited = set()
        q = collections.deque()
        q.append((beginWord, 1))
        while q:
            curr_word, step = q.popleft()
            if curr_word == endWord:
                return step
            visited.add(curr_word)
            for i in range(len(curr_word)):
                pattern = curr_word[0:i] + "*" + curr_word[i + 1:]
                for next_word in adjacency_list[pattern]:
                    if next_word not in visited:
                        q.append((next_word, step + 1))

        return 0
