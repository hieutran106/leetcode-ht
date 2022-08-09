from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        words_lens = list(map(lambda x: len(x), words))
        memo = {}
        # additional data structure to remember break points
        break_points = [None for i in range(len(words))]
        min_badness = self.findMinBadness(words, words_lens, maxWidth, len(words) - 1, memo, break_points)

        # split line
        return self.justify_paragraph(words, words_lens, maxWidth, break_points)

    def justify_paragraph(self, words: List[str], words_len: List[int], maxWidth: int, break_points: List[int]):
        """
        Go through break points array to create a line
        """
        paragraph = []
        start = 0
        for end in range(len(break_points)):
            if end == len(break_points) - 1 or break_points[end + 1] != break_points[start]:
                line_words = words[start: end + 1]
                # construct line for line_words
                justified_line = self.justify_line(line_words, maxWidth, end == len(break_points) - 1)
                paragraph.append(justified_line)
                start = end + 1

        return paragraph

    def justify_line(self, line_words: List[str], maxWidth: int, last_line: bool):
        # handle last line
        if last_line:
            line_str = ' '.join(line_words)
            line_str += ' ' * (maxWidth - len(line_str))
            return line_str

        # otherwise
        if len(line_words) == 1:
            line_str = line_words[0] + ' ' * (maxWidth - len(line_words[0]))
            return line_str

        words_lens = map(lambda w: len(w), line_words)
        spaces = maxWidth - sum(words_lens)
        even_space = spaces // (len(line_words) - 1)
        r = spaces % (len(line_words) - 1)

        line_str = ''
        for i in range(0, len(line_words) - 1):
            if i < r:
                padding = ' ' * (even_space + 1)
            else:
                padding = ' ' * even_space

            line_str += line_words[i] + padding

        line_str += line_words[-1]
        return line_str


    def findMinBadness(self, words,  words_lens: List[int], maxWidth: int, pos: int, memo, break_points):
        """
        From min badness from pos-th position
        """
        if pos < 0:
            return 0

        if pos in memo:
            return memo[pos]

        candidates = {}
        for j in range(pos, -1, -1):
            slice = words_lens[j:pos + 1]
            total_width = sum(slice)
            min_required_width = total_width + len(slice) - 1

            if min_required_width > maxWidth:
                break

            # otherwise, compute badness for the candidate
            additional_spaces = maxWidth - total_width + self.findMinBadness(words, words_lens, maxWidth, j - 1, memo, break_points)
            badness = additional_spaces
            candidates[j] = badness

        # Find the index where the min  happens
        arg_min = min(candidates, key=candidates.get)
        line_words = words[arg_min:pos + 1]
        line_str = self.justify_line(line_words, maxWidth, False)
        line_badness = maxWidth - sum(map(lambda w: len(w), line_words))
        # print(f"{pos=}: {arg_min=}, min badness={candidates[arg_min]}, for line :{[line_str]}, {line_badness=}")
        break_points[pos] = arg_min
        # memoize
        memo[pos] = candidates[arg_min]
        return candidates[arg_min]









