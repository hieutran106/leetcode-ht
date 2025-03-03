#include "../test/catch_amalgamated.hpp"

using namespace std;

class Solution
{
public:
    vector<int> twoSum(vector<int> &nums, int target)
    {
        return vector<int>{10, 20};
    }
};

TEST_CASE("Test case 1")
{
    Solution s;
    auto nums = vector<int>{2, 7, 11, 15};
    auto actual = s.twoSum(nums, 9);
    auto expect = vector<int>{0, 1};
    CHECK(actual == expect);
}

TEST_CASE("Test case 2")
{
    Solution s;
    auto nums = vector<int>{3, 2, 4};
    auto actual = s.twoSum(nums, 6);
    auto expect = vector<int>{1, 2};
    CHECK(actual == expect);
}