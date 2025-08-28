
#include <catch2/catch_test_macros.hpp>

// Date: 2025-08-26
// Problem: 3000 max_area_of_logest_diagonal_rect
using std::vector;

class Solution {
public:
    int areaOfMaxDiagonal(vector<vector<int>>& dimensions) {
        int ans = 0;
        long maxDiagonal = 0;
        for (vector<int>& rect:dimensions) {
            long diagonal = rect[0] * rect[0] + rect[1] * rect[1];
            if (diagonal > maxDiagonal) {
                maxDiagonal = diagonal;
                ans = rect[0] * rect[1];
            } else if (diagonal == maxDiagonal) {
                ans = std::max(ans, rect[0] * rect[1]);
            }
        }
        return ans;
    }
};

Solution s;
TEST_CASE("[3000] Test case 1", "") {
    vector<vector<int>> input = {{9, 3}, {8, 6}};
    auto actual = s.areaOfMaxDiagonal(input);
    REQUIRE(actual == 48);
}


TEST_CASE("[3000] Test case 2", "") {
    vector<vector<int>> input = {{4, 3}, {4, 3}};
    auto actual = s.areaOfMaxDiagonal(input);
    REQUIRE(actual == 12);
}

TEST_CASE("[3000] Test case 4", "") {
    vector<vector<int>> input = {{6, 5}, {8, 6}, {2, 10}, {8, 1}, {9, 2}, {3, 5}, {3, 5}};
    auto actual = s.areaOfMaxDiagonal(input);
    REQUIRE(actual == 20);
}

