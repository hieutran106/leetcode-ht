#include <catch2/catch_test_macros.hpp>
#include <vector>

using std::vector;

// Date: 2025-21-08
class Solution {
public:
    int countSquares(vector<vector<int> > &matrix) {
        size_t rows = matrix.size();
        size_t cols = matrix[0].size();

        // dp[i][j] is the number of square that has (i,j) as bottom-right
        vector<vector<int> > dp(rows, vector<int>(cols, 0));
        int ans = 0;
        for (size_t i = 0; i < rows; i++) {
            for (size_t j = 0; j < cols; j++) {
                if (matrix[i][j] == 0) {
                    dp[i][j] = 0;
                    continue;
                }
                if (i == 0 || j == 0) {
                    dp[i][j] = matrix[i][j];
                } else {
                    dp[i][j] = std::min({
                                   dp[i - 1][j - 1],
                                   dp[i - 1][j],
                                   dp[i][j - 1]
                               }) + 1;
                }


                ans += dp[i][j];
            }
        }

        return ans;
    }
};

TEST_CASE("Test case 1", "") {
    Solution s;
    vector<vector<int> > input = {{0, 1, 1, 1}, {1, 1, 1, 1}, {0, 1, 1, 1}};
    auto actual = s.countSquares(input);
    REQUIRE(actual == 15);
}


TEST_CASE("Test case 2", "") {
    Solution s;
    vector<vector<int> > input = {{1, 0, 1}, {1, 1, 0}, {1, 1, 0}};
    auto actual = s.countSquares(input);
    REQUIRE(actual == 7);
}

TEST_CASE("Test case 3", "") {
    Solution s;
    vector<vector<int> > input = {{1, 0}, {0, 1}};
    auto actual = s.countSquares(input);
    REQUIRE(actual == 2);
}

TEST_CASE("Test case 4", "") {
    Solution s;
    vector<vector<int> > input = {{1, 1}, {1, 1}};
    auto actual = s.countSquares(input);
    REQUIRE(actual == 5);
}
