#include "../test/catch_amalgamated.hpp"

using namespace std;

class Solution
{
public:
    bool divideArray(vector<int> &nums)
    {
        unordered_map<int, int> count;
        for (auto n : nums)
        {
            count[n] += 1;
        }
        for (const auto &pair : count)
        {
            if (pair.second % 2 == 1)
                return false;
        }
        return true;
    }
};

TEST_CASE("test_case_1")
{
    Solution s;
    auto nums = vector<int>{3, 2, 3, 2, 2, 2};
    auto actual = s.divideArray(nums);
    CHECK(actual == true);
}

TEST_CASE("test_case_2")
{
    Solution s;
    auto nums = vector<int>{1, 2, 3, 4};
    auto actual = s.divideArray(nums);
    CHECK(actual == false);
}
