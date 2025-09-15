
#include <catch2/catch_test_macros.hpp>

// Date: 2025-09-15
// Problem: 2351 first_letter_appear_twice
using std::vector;
using std::string;

class Solution {
public:
    char repeatedCharacter(string s) {
        std::bitset<26> bitset;
        for (auto c: s) {
            if (bitset.test(c - 'a')) {
                return c;
            }
            bitset.set(c - 'a');
        }
        return 'a';
    }
};

Solution s;
TEST_CASE("[2351] Test case 1", "") {
    auto actual = s.repeatedCharacter("abccbaacz");
    REQUIRE(actual == 'c');
}


TEST_CASE("[2351] Test case 2", "") {
    auto actual = s.repeatedCharacter("abcdd");
    REQUIRE(actual == 'd');
}

TEST_CASE("[2351] Test case 3", "") {
    auto actual = s.repeatedCharacter("aa");
    REQUIRE(actual == 'a');
}

