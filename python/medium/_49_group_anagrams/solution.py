from typing import List

def get_anagram_array(str: str) -> List[int]:
    anagram_array = [0] * 26
    for c in str:
        index = ord(c) - ord('a')
        anagram_array[index] += 1

    return anagram_array

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for str in strs:
            anagram_array = get_anagram_array(str)
            key = tuple(anagram_array)
            if key not in dict:
                dict[key] = [str]
            else:
                array = dict[key]
                array.append(str)

        result = list(dict.values())
        return result


