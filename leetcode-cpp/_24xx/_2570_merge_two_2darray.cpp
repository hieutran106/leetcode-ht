#include "../test/htcatch.h"
#include <vector>
#include <limits>
#include <iostream>
#include <algorithm>
#include <iterator>

using namespace std;

class Solution
{
public:
    vector<vector<int>> mergeArrays(vector<vector<int>> &nums1, vector<vector<int>> &nums2)
    {
        std::vector<int>::size_type p1{0};
        std::vector<int>::size_type p2{0};
        vector<vector<int>> ans{};
        while (p1 < nums1.size() || p2 < nums2.size())
        {
            int id1{numeric_limits<int>::max()};
            int val1{0};
            if (p1 < nums1.size())
            {
                id1 = nums1.at(p1).at(0);
                val1 = nums1.at(p1).at(1);
            }

            int id2{numeric_limits<int>::max()};
            int val2{0};
            if (p2 < nums2.size())
            {
                id2 = nums2.at(p2).at(0);
                val2 = nums2.at(p2).at(1);
            }

            if (id1 < id2)
            {
                ans.push_back(vector<int>{id1, val1});
                p1++;
            }
            else if (id1 == id2)
            {
                ans.push_back(vector<int>{id1, val1 + val2});
                p1++;
                p2++;
            }
            else
            {
                ans.push_back(vector<int>{id2, val2});
                p2++;
            }
        }
        for (std::vector<int>::size_type i = 0; i < ans.size(); ++i)
        {
            std::cout << "[" << ans[i].at(0) << ", " << ans[i].at(1) << "]";
        }
        std::cout << std::endl;
        return ans;
    }
};

TEST(test_case_1)
{
    Solution s;
    vector<vector<int>> nums1 = {
        {1, 2},
        {2, 3},
        {4, 5}};
    vector<vector<int>> nums2 = {{1, 4}, {3, 2}, {4, 1}};
    auto actual = s.mergeArrays(nums1, nums2);

    vector<vector<int>> expect = {{1, 6}, {2, 3}, {3, 2}, {4, 6}};
    ASSERT_TRUE(actual == expect);
}
TEST(test_case_2)
{
    Solution s;
    vector<vector<int>> nums1 = {
        {2, 4},
        {3, 6},
        {5, 5}};
    vector<vector<int>> nums2 = {{1, 3}, {4, 3}};
    auto actual = s.mergeArrays(nums1, nums2);

    vector<vector<int>> expect = {{1, 3}, {2, 4}, {3, 6}, {4, 3}, {5, 5}};
    ASSERT_TRUE(actual == expect);
}

TEST_MAIN()