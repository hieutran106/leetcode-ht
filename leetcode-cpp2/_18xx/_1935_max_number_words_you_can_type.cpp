
#include <catch2/catch_test_macros.hpp>

// Date: 2025-09-15
// Problem: 1935 max_number_words_you_can_type
using std::vector;
using std::string;

vector<string> splitBySpace(const string input) {
    std::istringstream iss(input);
    vector<string> result {std::istream_iterator<std::string>{iss}, std::istream_iterator<std::string>{}};
    return result;
}

class Solution {
public:
    int canBeTypedWords(string text, string brokenLetters) {
        auto words = splitBySpace(text);
        std::bitset<26> bitset;
        for (auto c: brokenLetters) {
            bitset.set(c - 'a');
        }

        int ans = 0;
        for (auto& w: words) {
            bool broken  = false;
            for (auto c: w) {
                if (bitset.test(c - 'a')) {
                    broken = true;
                    break;
                }
            }
            if (!broken) {
                ans += 1;
            }
        }
        return ans;
    }
};

Solution s;
TEST_CASE("[1935] Test case 1", "") {
    auto actual = s.canBeTypedWords("hello world",  "ad");
    REQUIRE(actual == 1);
}


TEST_CASE("[1935] Test case 2", "") {
    auto actual = s.canBeTypedWords("leet code",  "lt");
    REQUIRE(actual == 1);
}

TEST_CASE("[1935] Test case 3", "") {
    auto actual = s.canBeTypedWords("leet code",  "e");
    REQUIRE(actual == 0);
}

