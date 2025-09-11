
#include <catch2/catch_test_macros.hpp>
#include <algorithm>

// Date: 2025-09-11
// Problem: 2785 sort_vowels_in_str
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
    string sortVowels(string s) {
        vector<char> vowels;
        for (auto c: s) {
            if (isVowel(c)) {
                vowels.push_back(c);
            }
        }
        std::sort(vowels.begin(), vowels.end());

        int i = 0;
        std::string ans;
        ans.reserve(s.size());
        for (auto c:s) {
            if (isVowel(c)) {
                ans.push_back(vowels[i]);
                i++;
                continue;
            }
            ans.push_back(c);
        }
        return ans;
    }
};

Solution s;
TEST_CASE("[2785] Test case 1", "") {
    auto actual = s.sortVowels("lEetcOde");
    REQUIRE(actual == "lEOtcede");
}


TEST_CASE("[2785] Test case 2", "") {
    auto actual = s.sortVowels("lYmpH");
    REQUIRE(actual == "lYmpH");
}

