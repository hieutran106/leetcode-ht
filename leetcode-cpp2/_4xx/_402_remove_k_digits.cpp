
#include <catch2/catch_test_macros.hpp>

// Date: 2025-08-28
// Problem: 402 remove_k_digits
using std::string;
using std::vector;

void trimLeadingZeros(vector<char>& chars) {
    auto it = std::find_if(chars.begin(), chars.end(), [](char c) {
        return c != '0';
    });

    chars.erase(chars.begin(), it);
    if (chars.empty()) {
        chars.push_back('0'); // keep a single zero
    }
}
class Solution {
public:
    string removeKdigits(string num, int k) {
        // Increasing stack with a maximum of k removal
        int removeCount = k;
        vector<char> stack;
        for (char& c: num) {
            while (!stack.empty() && c < stack.back() && removeCount > 0) {
                stack.pop_back();
                removeCount--;
            }
            stack.push_back(c);
        }
        while (removeCount > 0) {
            stack.pop_back();
            removeCount--;
        }
        trimLeadingZeros(stack);
        std::string ans(stack.begin(), stack.end());
        return ans;
    }
};

Solution s;
TEST_CASE("[402] Test case 1", "") {
    auto actual = s.removeKdigits("1432219", 3);
    REQUIRE(actual == "1219");
}


TEST_CASE("[402] Test case 2", "") {
    auto actual = s.removeKdigits("10200", 1);
    REQUIRE(actual == "200");
}

TEST_CASE("[402] Test case 3", "") {
    auto actual = s.removeKdigits("10", 2);
    REQUIRE(actual == "0");
}

TEST_CASE("[402] Test case 4", "") {
    auto actual = s.removeKdigits("0", 1);
    REQUIRE(actual == "0");
}

TEST_CASE("[402] Test case 5", "") {
    auto actual = s.removeKdigits("11100", 2);
    REQUIRE(actual == "100");
}

TEST_CASE("[402] Test case 6", "") {
    auto actual = s.removeKdigits("00000", 1);
    REQUIRE(actual == "0");
}

TEST_CASE("[402] Test case 7", "") {
    auto actual = s.removeKdigits("9999", 4);
    REQUIRE(actual == "0");
}

TEST_CASE("[402] Test case 8", "") {
    auto actual = s.removeKdigits("55515", 4);
    REQUIRE(actual == "1");
}

TEST_CASE("[402] Test case 9", "") {
    auto actual = s.removeKdigits("112", 1);
    REQUIRE(actual == "11");
}

