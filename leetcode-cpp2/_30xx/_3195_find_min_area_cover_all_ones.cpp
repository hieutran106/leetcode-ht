
#include <catch2/catch_test_macros.hpp>

// Date: 2025-22-08
using std::vector;


class Solution {
public:
    int minimumArea(vector<vector<int>>& grid) {
        size_t rows = grid.size();
        size_t cols = grid[0].size();
        size_t r1 = 1000, r2 = 0;
        size_t c1 = 1000, c2 = 0;

        for (size_t i = 0; i < rows; i++) {
            for (size_t j = 0; j < cols; j++) {
                if (grid[i][j] == 1) {
                    r1 = std::min(r1, i);
                    r2 = std::max(r2, i);

                    c1 = std::min(c1, j);
                    c2 = std::max(c2, j);
                }
            }
        }

        int ans = static_cast<int>((r2 - r1 +1) * (c2 - c1 + 1));

        return ans;
    }
};

Solution s;
TEST_CASE("Test case 1", "") {
    vector<vector<int>> grid = {{0, 1, 0}, {1, 0, 1}};
    auto actual = s.minimumArea(grid);
    REQUIRE(actual == 6);
}

TEST_CASE("Test case 2", "") {
    vector<vector<int>> grid = {{1, 0}, {0, 0}};
    auto actual = s.minimumArea(grid);
    REQUIRE(actual == 1);
}

