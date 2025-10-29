
#include <catch2/catch_test_macros.hpp>

// Date: 2025-10-29
// Problem: 3370 smallest_number_with_set_bits
using std::vector;
using std::string;

class Solution {
public:
    int smallestNumber(int n) {
        int bitCount = 0;
        while (n > 1) {
            n = n /2;
            bitCount++;
        }
        auto ans = static_cast<int>(std::pow(2, bitCount +1)) - 1;
        return ans;
    }
};

Solution s;
TEST_CASE("[3370] Test case 1", "") {
    auto actual = s.smallestNumber(5);
    REQUIRE(actual == 7);
}


TEST_CASE("[3370] Test case 2", "") {
    auto actual = s.smallestNumber(10);
    REQUIRE(actual == 15);
}

TEST_CASE("[3370] Test case 3", "") {
    auto actual = s.smallestNumber(3);
    REQUIRE(actual == 3);
}

TEST_CASE("[3370] Test case 4", "") {
    auto actual = s.smallestNumber(2);
    REQUIRE(actual == 3);
}

