// _191_count_1_bit created on 8/12/25
#include <catch2/catch_test_macros.hpp>

class Solution {
public:
    int hammingWeight(int n) {
        int ans = 0;
        while (n > 0) {
            int r = n % 2;
            if (r == 1) {
                ans++;
            }
            n = n /2;
        }
        return ans;
    }
};

TEST_CASE("Test case 1", "") {
    Solution s;
    auto actual = s.hammingWeight(11);
    REQUIRE(actual == 3);
}


TEST_CASE("Test case 2", "") {
    Solution s;
    auto actual = s.hammingWeight(128);
    REQUIRE(actual == 1);
}

TEST_CASE("Test case 3", "") {
    Solution s;
    auto actual = s.hammingWeight(2147483645);
    REQUIRE(actual == 30);
}


