
#include <catch2/catch_test_macros.hpp>
#include <vector>

using std::vector;
// Date: 2025-21-08
class Solution {
public:
    int numSubmat(vector<vector<int>>& mat) {
        // Brute-force solution
        auto rows = mat.size();
        auto cols = mat[0].size();
        int ans = 0;

        for (size_t i = 0 ; i < rows; i ++) {
            for (size_t j = 0; j < cols; j++) {
                if (mat[i][j] == 1) {
                    ans += helper(mat, i, j);
                }
            }
        }

        return ans;
    }

    // count all submatrices with top-left corner at (r,c)
    int helper(vector<vector<int>>& mat, size_t r, size_t c) {
        size_t rows = mat.size();
        size_t bound = mat[0].size();
        int count = 0;
        for (size_t i = r; i < rows; i++) {
            for (size_t j = c; j < bound;j ++) {
                if (mat[i][j] == 1) {
                    count++;
                } else {
                    bound = j;
                }
            }
        }
        return count;
    }
};

TEST_CASE("Test case 1", "") {
    Solution s;
    vector<vector<int>> input{{1, 0, 1}, {1, 1, 0}, {1, 1, 0}};
    int actual = s.numSubmat(input);
    REQUIRE(actual == 13);
}


TEST_CASE("Test case 2", "") {
    Solution s;
    vector<vector<int>> input{{0, 1, 1, 0}, {0, 1, 1, 1}, {1, 1, 1, 0}};
    int actual = s.numSubmat(input);
    REQUIRE(actual == 24);
}

TEST_CASE("Test case 3", "") {
    Solution s;
    vector<vector<int>> input{{1, 1}, {1, 1}};
    int actual = s.numSubmat(input);
    REQUIRE(actual == 9);
}


TEST_CASE("Test case 4", "") {
    Solution s;
    vector<vector<int>> input = {{1, 0}, {1, 1}};
    int actual = s.numSubmat(input);
    REQUIRE(actual == 5);
}

