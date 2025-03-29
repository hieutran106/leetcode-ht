#include "../test/catch_amalgamated.hpp"
#include <map>

using namespace std;

class Solution
{
public:
    vector<int> twoSum(vector<int> &nums, int target)
    {
        map<int, int> d;
        for (size_t i = 0; i < nums.size(); i++)
        {
            auto key = target - nums.at(i);
            if (d.find(key) != d.end())
            {
                return vector<int>{d[key], (int)i};
            }
            else
            {
                d.insert(make_pair(nums.at(i), i));
            }
        }
        return vector<int>{0, 1};
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