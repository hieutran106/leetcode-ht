#include "../test/catch_amalgamated.hpp"

using namespace std;

class Solution
{
public:
    vector<int> pivotArray(vector<int> &nums, int pivot)
    {
        vector<int> less{};
        vector<int> equal{};
        vector<int> greater{};
        for (size_t i = 0; i < nums.size(); i++)
        {
            auto n = nums.at(i);
            if (n < pivot)
            {
                less.push_back(n);
            }
            else if (n == pivot)
            {
                equal.push_back(n);
            }
            else
            {
                greater.push_back(n);
            }
        }
        vector<int> ans{};
        ans.reserve(less.size() + equal.size() + greater.size());
        ans.insert(ans.end(), less.begin(), less.end());
        ans.insert(ans.end(), equal.begin(), equal.end());
        ans.insert(ans.end(), greater.begin(), greater.end());
        return ans;
    }
};

TEST_CASE("test_case_1")
{
    Solution s;
    auto nums = vector<int>{9, 12, 5, 10, 14, 3, 10};
    auto expect = vector<int>{9, 5, 3, 10, 10, 12, 14};
    auto actual = s.pivotArray(nums, 10);
    CHECK(expect == actual);
}
TEST_CASE("test_case_2")
{
    Solution s;
    auto nums = vector<int>{9, 12, 5, 10, 14, 3, 10};
    auto expect = vector<int>{9, 5, 3, 10, 10, 12, 14};
    auto actual = s.pivotArray(nums, 10);
    CHECK(expect == actual);
}
