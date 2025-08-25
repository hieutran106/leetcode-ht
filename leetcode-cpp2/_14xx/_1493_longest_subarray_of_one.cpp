
#include <catch2/catch_test_macros.hpp>

// Date: 2025-08-25
// Problem: 1493 longest_subarray_of_one
using std::vector;

class Solution {
public:
    int longestSubarray(vector<int>& nums) {
        // Maintain a sliding window where there is at most one zero in it
        int l = 0;
        int zeroCount = 0;
        int ans = 0;
        for (int r = 0; r < nums.size(); r++) {
            if (nums[r] == 0) {
                zeroCount++;
            }
            while (zeroCount > 1) {
                if (nums[l] == 0) {
                    zeroCount--;
                }
                l++;
            }
            ans = std::max(ans, r - l + 1 - 1); // We need to remove at least 1 element
        }
        return ans;
    }
};

Solution s;
TEST_CASE("[1493] Test case 1", "") {
    vector<int> input = {0};
    auto actual = s.longestSubarray(input);
    REQUIRE(actual == 0);
}


TEST_CASE("[1493] Test case 2", "") {
    vector<int> input = {1,1,0,1};
    auto actual = s.longestSubarray(input);
    REQUIRE(actual == 3);
}

TEST_CASE("[1493] Test case 3", "") {
    vector<int> input = {0,1,1,1,0,1,1,0,1};
    auto actual = s.longestSubarray(input);
    REQUIRE(actual == 5);
}

TEST_CASE("[1493] Test case 4", "") {
    vector<int> input = {1, 1, 1};
    auto actual = s.longestSubarray(input);
    REQUIRE(actual == 2);
}

TEST_CASE("[1493] Test case 5", "") {
    vector<int> input = {1};
    auto actual = s.longestSubarray(input);
    REQUIRE(actual == 0);
}

TEST_CASE("[1493] Test case 6", "") {
    vector<int> input = {1, 0, 0, 0, 0};
    auto actual = s.longestSubarray(input);
    REQUIRE(actual == 1);
}

