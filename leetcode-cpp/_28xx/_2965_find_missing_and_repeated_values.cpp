#include "../test/catch_amalgamated.hpp"
#include <iostream>
#include <set>

using namespace std;

class Solution
{
public:
    vector<int> findMissingAndRepeatedValues(vector<vector<int>> &grid)
    {

        size_t rows = grid.size();
        vector<int> seen(rows * rows, 0);

        for (size_t i = 0; i < rows; i++)
        {
            for (size_t j = 0; j < rows; j++)
            {
                int v = grid.at(i).at(j);

                seen.at(v - 1) += 1;
            }
        }

        int a{0};
        int b{0};
        for (size_t i = 0; i < rows * rows; i++)
        {
            if (seen.at(i) == 2)
            {
                a = (int)i;
            }
            else if (seen.at(i) == 0)
            {
                b = (int)i;
            }
        }

        return vector<int>{a + 1, b + 1};
    }
};

TEST_CASE("test_case_1")
{
    Solution s;
    auto nums = vector<vector<int>>{{1, 3}, {2, 2}};
    auto actual = s.findMissingAndRepeatedValues(nums);
    CHECK(actual == vector<int>{2, 4});
}

TEST_CASE("test_case_2")
{
    Solution s;
    auto nums = vector<vector<int>>{{9, 1, 7}, {8, 9, 2}, {3, 4, 6}};
    auto actual = s.findMissingAndRepeatedValues(nums);
    CHECK(actual == vector<int>{9, 5});
}
