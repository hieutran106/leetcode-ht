
#include <catch2/catch_test_macros.hpp>

// Date: 2025-08-25
// Problem: 1004 max_consecutive_one
using std::vector;
class Solution {
public:
    int longestOnes(vector<int>& nums, int k) {
        // Maintain a sliding window that has at most k zero
        int zeroCount = 0;
        int l = 0;
        int ans = 0;
        for (int r = 0; r < nums.size(); r++) {
            if (nums[r] == 0) {
                zeroCount++;
            }
            while (zeroCount > k) {
                if (nums[l] == 0) {
                    zeroCount--;
                }
                l++;
            }
            ans = std::max(ans, r - l + 1);
        }
        return ans;
    }
};

Solution s;
TEST_CASE("[1004] Test case 1", "") {
    vector<int> input = { 1,1,1,0,0,0,1,1,1,1,0};
    auto actual = s.longestOnes(input, 2);
    REQUIRE(actual == 6);
}


TEST_CASE("[1004] Test case 2", "") {
    vector<int> input = { 0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1};
    auto actual = s.longestOnes(input, 3);
    REQUIRE(actual == 10);
}

TEST_CASE("[1004] Test case 3", "") {
    vector<int> input = { 0 };
    auto actual = s.longestOnes(input, 0);
    REQUIRE(actual == 0);
}

TEST_CASE("[1004] Test case 4", "") {
    vector<int> input = { 0 };
    auto actual = s.longestOnes(input, 1);
    REQUIRE(actual == 1);
}

