
#include <catch2/catch_test_macros.hpp>

// Date: 2025-08-26
// Problem: 485 max_consecutive_ones
using std::vector;

class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        // Maintain a sliding window that contains no zeros
        int zeroCount = 0;
        int l = 0;
        int ans = 0;
        for (int r = 0; r < nums.size(); r++) {
            if (nums[r] == 0) {
                zeroCount++;
            }
            while (zeroCount > 0) {
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
TEST_CASE("[485] Test case 1", "") {
    vector<int> nums = {1,1,0,1,1,1};
    auto actual = s.findMaxConsecutiveOnes(nums);
    REQUIRE(actual == 3);
}


TEST_CASE("[485] Test case 2", "") {
    vector<int> nums = {1,0,1,1,0,1};
    auto actual = s.findMaxConsecutiveOnes(nums);
    REQUIRE(actual == 2);
}

TEST_CASE("[485] Test case 3", "") {
    vector<int> nums = {0};
    auto actual = s.findMaxConsecutiveOnes(nums);
    REQUIRE(actual == 0);
}

TEST_CASE("[485] Test case 4", "") {
    vector<int> nums = {1};
    auto actual = s.findMaxConsecutiveOnes(nums);
    REQUIRE(actual == 1);
}

TEST_CASE("[485] Test case 5", "") {
    vector<int> nums = {0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1};
    auto actual = s.findMaxConsecutiveOnes(nums);
    REQUIRE(actual == 4);
}

