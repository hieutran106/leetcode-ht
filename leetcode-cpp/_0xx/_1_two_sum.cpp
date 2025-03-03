#include "../test/htcatch.h"
#include <vector>
#include <iostream>
#include <iterator>

using namespace std;

class Solution
{
public:
    vector<int> twoSum(vector<int> &nums, int target)
    {
        return vector<int>{1, 2};
    }
};

TEST(test_case_1)
{
    Solution s;
    auto nums = vector<int>{2, 7, 11, 15};
    auto actual = s.twoSum(nums, 9);
    auto expect = vector<int>{0, 1};
    ASSERT_TRUE(actual == expect);
}
TEST(test_case_2)
{
    Solution s;
    auto nums = vector<int>{3, 2, 4};
    auto actual = s.twoSum(nums, 6);
    auto expect = vector<int>{1, 2};
    ASSERT_TRUE(actual == expect);
}
TEST(test_case_3)
{
    Solution s;
    auto nums = vector<int>{3, 3};
    auto actual = s.twoSum(nums, 6);
    auto expect = vector<int>{0, 1};
    ASSERT_TRUE(actual == expect);
}

TEST_MAIN()
