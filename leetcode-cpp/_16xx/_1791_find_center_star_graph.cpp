#include "../test/htcatch.h"
#include <vector>

using namespace std;

class Solution
{
public:
    int findCenter(vector<vector<int>> &edges)
    {
        if (edges[0][0] == edges[1][0] || edges[0][0] == edges[1][1])
        {
            return edges[0][0];
        }
        return edges[0][1];
    }
};

TEST(test_case_1)
{
    Solution s;
    vector<vector<int>> mockEdges = {
        {1, 2},
        {2, 3},
        {4, 2}};
    int actual = s.findCenter(mockEdges);
    ASSERT_EQUAL(actual, 2);
}
TEST(test_case_2)
{
    Solution s;
    vector<vector<int>> mockEdges = {{1, 2}, {5, 1}, {1, 3}, {1, 4}};
    auto actual = s.findCenter(mockEdges);
    ASSERT_EQUAL(actual, 1);
}

TEST_MAIN()