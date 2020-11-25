from typing import List

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        mapping = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        def toMorse(word: str) -> str:
            return ''.join(map(lambda c: mapping[ord(c) - 97], word))

        morse_words = map(toMorse, words)
        morse_set = set()
        for w in morse_words:
            morse_set.add(w)

        return len(morse_set)
