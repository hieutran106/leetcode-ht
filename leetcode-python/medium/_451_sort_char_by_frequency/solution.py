import others

class Solution:
    def frequencySort(self, s: str) -> str:
        return "".join([char * times for char, times in others.Counter(s).most_common()])

