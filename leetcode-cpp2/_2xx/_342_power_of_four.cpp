
#include <catch2/catch_test_macros.hpp>

// Date: 2025-15-08
constexpr std::array<int, 16> values = []() constexpr {
    std::array<int, 16> arr = {1};
    for (int i = 1; i < 16; ++i)
        arr[i] = arr[i - 1] * 4;
    return arr;
}();

class Solution {
public:
    bool isPowerOfFour(int n) {
        for (int v: values) {
            if (n == v) return true;
        }
        return false;
    }
};



TEST_CASE("Test case 1", "") {
    auto actual = Solution().isPowerOfFour(16);
    REQUIRE(actual == true);
}


TEST_CASE("Test case 2", "") {
    auto actual = Solution().isPowerOfFour(5);
    REQUIRE(actual == false);
}

TEST_CASE("Test case 3", "") {
    auto actual = Solution().isPowerOfFour(1);
    REQUIRE(actual == true);
}

TEST_CASE("Test case 4", "") {
    auto actual = Solution().isPowerOfFour(256);
    REQUIRE(actual == true);
}

TEST_CASE("Test case 5", "") {
    auto actual = Solution().isPowerOfFour(257);
    REQUIRE(actual == false);
}

