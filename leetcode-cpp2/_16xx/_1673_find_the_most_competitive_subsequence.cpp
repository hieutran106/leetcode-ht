
#include <catch2/catch_test_macros.hpp>
#include "../utils/serde.cpp"
// Date: 2025-08-28
// Problem: 1673 find_the_most_competitive_subsequence
using std::vector;

class Solution {
public:
    vector<int> mostCompetitive(vector<int>& nums, int k) {
        // Try to form the smallest subsequence, in which we have at most len(nums) - k removal
        // Use increasing stack
        int removeCount = nums.size() - k;
        vector<int> stack;

        for (int& n: nums) {
            while (!stack.empty() && n < stack.back() && removeCount > 0) {
                stack.pop_back();
                removeCount--;
            }
            stack.push_back(n);
        }
        vector<int> ans;
        ans.reserve(k);
        for (int i =0; i < k; i++) {
            ans.push_back(stack[i]);
        }
        return ans;
    }
};

Solution s;
TEST_CASE("[1673] Test case 1", "") {
    auto nums = parseVector("3,5,2,6");
    auto actual = s.mostCompetitive(nums, 2);
    REQUIRE(actual == vector<int>{2, 6});
}


TEST_CASE("[1673] Test case 2", "") {
    auto nums = parseVector("[2,4,3,3,5,4,9,6]");
    auto actual = s.mostCompetitive(nums, 4);
    REQUIRE(actual == vector<int>{2,3,3,4});
}

TEST_CASE("[1673] Test case 3", "") {
    auto nums = parseVector("[1]");
    auto actual = s.mostCompetitive(nums, 1);
    REQUIRE(actual == vector<int>{1});
}

TEST_CASE("[1673] Test case 4", "") {
    auto nums = parseVector("[3, 2, 0, 4, 3, 1]");
    auto actual = s.mostCompetitive(nums, 2);
    REQUIRE(actual == vector<int>{0, 1});
}

TEST_CASE("[1673] Test case 5", "") {
    auto nums = parseVector("[9, 8, 7, 2, 3, 4]");
    auto actual = s.mostCompetitive(nums, 5);
    REQUIRE(actual == vector<int>{8, 7, 2, 3, 4});
}

