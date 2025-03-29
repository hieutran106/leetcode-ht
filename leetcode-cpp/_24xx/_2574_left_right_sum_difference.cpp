#include <numeric>

#include "../test/catch_amalgamated.hpp"
using namespace std;

class Solution {
   public:
    vector<int> leftRightDifference(vector<int>& nums) {
        auto sum = std::accumulate(nums.begin(), nums.end(), 0L);
        auto sumLeft = sum;
        long sumRight = 0;
        auto ans = vector<int>{};
        for (auto n : nums) {
            sumLeft = sumLeft - n;
            ans.push_back(abs((int)(sumRight - sumLeft)));
            sumRight += n;
        }
        return ans;
    }
};

TEST_CASE("test_case_1") {
    Solution s;
    auto nums = vector<int>{10, 4, 8, 3};
    auto expect = vector<int>{15, 1, 11, 22};
    auto actual = s.leftRightDifference(nums);
    CHECK(actual == expect);
}

TEST_CASE("test_case_2") {
    Solution s;
    auto nums = vector<int>{1};
    auto expect = vector<int>{0};
    auto actual = s.leftRightDifference(nums);
    CHECK(actual == expect);
}
