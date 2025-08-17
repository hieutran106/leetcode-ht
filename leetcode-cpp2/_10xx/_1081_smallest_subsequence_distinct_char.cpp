
#include <catch2/catch_test_macros.hpp>
#include <stack>
#include <map>
// Date: 2025-16-08
using namespace std;

class Solution {
public:
    string smallestSubsequence(string s) {
        map<char, size_t> lastSeen;
        for (size_t i =0; i < s.size(); i++) {
            lastSeen[s[i]] = i;
        }

        vector<char> stack;
        for (size_t i =0; i < s.size(); i++) {
            // Track if cur char is in the stack to ensure uniqueness
            if (std::find(stack.begin(), stack.end(), s[i]) != stack.end()) {
                continue;
            }
            // If previously seen char is greater,
            // and the previously seen shows up after current position
            // we can use previous char later => pop from the stack
            while (!stack.empty() && s[i] < stack.back() && lastSeen[stack.back()] > i) {
                stack.pop_back();
            }
            stack.push_back(s[i]);
        }

        string res(stack.begin(), stack.end());
        return res;
    }
};

TEST_CASE("Test case 1", "") {
    Solution s;
    auto actual = s.smallestSubsequence("bcabc");
    REQUIRE(actual == "abc");
}


TEST_CASE("Test case 2", "") {
    Solution s;
    auto actual = s.smallestSubsequence("cbacdcbc");
    REQUIRE(actual == "acdb");
}

TEST_CASE("Test case 3", "") {
    Solution s;
    auto actual = s.smallestSubsequence("zyxyabz");
    REQUIRE(actual == "xyabz");
}

TEST_CASE("Test case 4", "") {
    Solution s;
    auto actual = s.smallestSubsequence("bdacbbcd");
    REQUIRE(actual == "abcd");
}

TEST_CASE("Test case 5", "") {
    Solution s;
    auto actual = s.smallestSubsequence("cdadabcc");
    REQUIRE(actual == "adbc");
}


