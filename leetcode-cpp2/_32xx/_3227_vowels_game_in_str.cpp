
#include <catch2/catch_test_macros.hpp>

// Date: 2025-09-15
// Problem: 3227 vowels_game_in_str
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
    bool doesAliceWin(string s) {
        int vowelCount = 0;
        for (char c: s) {
            if (isVowel(c)) {
                vowelCount++;
            }
        }
        if (vowelCount == 0) return false;
        return true;
    }
};

Solution s;
TEST_CASE("[3227] Test case 1", "") {
    auto actual = s.doesAliceWin("leetcoder");
    REQUIRE(actual == true);
}


TEST_CASE("[3227] Test case 2", "") {
    auto actual = s.doesAliceWin("bbcd");
    REQUIRE(actual == false);
}

TEST_CASE("[3227] Test case 3", "") {
    auto actual = s.doesAliceWin("xxxxaei");
    REQUIRE(actual == true);
}

