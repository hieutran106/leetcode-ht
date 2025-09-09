
#include <catch2/catch_test_macros.hpp>

// Date: 2025-09-09
// Problem: 2327 number_people_aware_secret
using std::vector;
using std::string;

class Solution {
public:
    int peopleAwareOfSecret(int n, int delay, int forget) {
        // to submit change n+ 1 to n+2, and forget + 1 to forget + 2
        // vector dp(n + 2, vector<int>(forget + 2, 0));
        vector dp(n + 1, vector<int>(forget + 1, 0));
        long MOD = 1'000'000'007L;
        dp[1][forget] = 1;
        for (int i = 2; i <= n; i++) {
            long sharable = 0;
            for (int j = 1; j <= forget; j++) {

                dp[i][j] = dp[i-1][j+1];
                if (j <= forget - delay) {
                    sharable = (sharable + dp[i-1][j+1]) % MOD;
                }
            }
            dp[i][forget] = static_cast<int>(sharable);
        }
        int ans = 0;
        for (int j = 1; j <= forget; j++) {
            ans = (ans + dp[n][j]) % MOD;
        }
        return ans;
    }
};

Solution s;
TEST_CASE("[2327] Test case 1", "") {
    auto actual = s.peopleAwareOfSecret(6, 2, 4);
    REQUIRE(actual == 5);
}


TEST_CASE("[2327] Test case 2", "") {
    auto actual = s.peopleAwareOfSecret(4, 1, 3);
    REQUIRE(actual == 6);
}

TEST_CASE("[2327] Test case 3", "") {
    auto actual = s.peopleAwareOfSecret(2, 1, 2);
    REQUIRE(actual == 2);
}

TEST_CASE("[2327] Test case 4", "") {
    auto actual = s.peopleAwareOfSecret(50, 5, 8);
    REQUIRE(actual == 6757);
}

