
#include <catch2/catch_test_macros.hpp>

// Date: 2025-15-08
using namespace std;

class Solution {
public:
    string largestGoodInteger(string num) {
        char res = 0;
        for (int i = 2; i < num.size(); i++) {
            if (num[i] == num[i-1] and num[i-1] == num[i-2]) {
                res = std::max(res, num[i]);
            }
        }
        if (res == 0) return "";
        return string(3, res);
    }
};

TEST_CASE("Test case 1", "") {
    Solution s;
    auto actual = s.largestGoodInteger("6777133339");
    REQUIRE(actual == "777");
}


TEST_CASE("Test case 2", "") {
    Solution s;
    auto actual = s.largestGoodInteger("2300019");
    REQUIRE(actual == "000");
}

TEST_CASE("Test case 3", "") {
    Solution s;
    auto actual = s.largestGoodInteger("42352338");
    REQUIRE(actual == "");
}


TEST_CASE("Test case 4", "") {
    Solution s;
    auto actual = s.largestGoodInteger("00045667888000999");
    REQUIRE(actual == "999");
}

TEST_CASE("Test case 5", "") {
    Solution s;
    auto actual = s.largestGoodInteger("4566790000");
    REQUIRE(actual == "000");
}

TEST_CASE("Test case 6", "") {
    Solution s;
    auto actual = s.largestGoodInteger("3233333367840000009999999999543545");
    REQUIRE(actual == "999");
}

