
#include <catch2/catch_test_macros.hpp>

// Date: 2025-09-11
// Problem: 345 reverse_vowels_of_str
using std::vector;
using std::string;

bool isVowel(char c) {
    switch (c) {
        case 'A': case 'E': case 'I': case 'O': case 'U':
        case 'a': case 'e': case 'i': case 'o': case 'u':
            return true;
        default:
            return false;
    }
}

class Solution {
public:
    string reverseVowels(string s) {
        vector<char> vowels;
        for (auto c:s) {
            if (isVowel(c)) {
                vowels.push_back(c);
            }
        }
        std::string ans;
        int i = vowels.size() - 1;
        for (auto c:s) {
            if (isVowel(c)) {
                ans.push_back(vowels[i]);
                i--;
                continue;
            }
            ans.push_back(c);
        }
        return ans;
    }
};

Solution s;
TEST_CASE("[345] Test case 1", "") {
    auto actual = s.reverseVowels("IceCreAm");
    REQUIRE(actual == "AceCreIm");
}


TEST_CASE("[345] Test case 2", "") {
    auto actual = s.reverseVowels("leetcode");
    REQUIRE(actual == "leotcede");
}

TEST_CASE("[345] Test case 3", "") {
    auto actual = s.reverseVowels("a");
    REQUIRE(actual == "a");
}

