
#include <catch2/catch_test_macros.hpp>
#include <vector>
#include <numeric>

// Date: 2025-22-08
using std::vector;

class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        int ans = 0;
        vector<int> nextLess = this->nextLess(heights);
        vector<int> prevLess = this->prevLess(heights);
        int n = static_cast<int>(heights.size());
        for (int i =0; i < n; i++) {
            int curr = (nextLess[i] - prevLess[i] - 1) * heights[i];
            ans = std::max(ans, curr);
        }
        return ans;
    }

    vector<int> nextLess(vector<int>& heights) {
        int n = static_cast<int>(heights.size());
        vector<int> res(n, n); // default to n when no smaller element to the right
        vector<std::pair<int, int>> stack; // increasing stack (index, value)
        for (int i =0; i < n; i++) {
            int h = heights[i];
            while (!stack.empty() && h < stack.back().second) {
                res[stack.back().first] = i;
                stack.pop_back();
            }
            stack.emplace_back(i, h);
        }
        return res;
    }

    vector<int> prevLess(vector<int>& heights) {
        int n = static_cast<int>(heights.size());
        vector<int> res(n, -1); // default to -1 when no prev smaller element
        vector<std::pair<int, int>> stack; // increasing stack (index, value)
        for (int i = 0; i < n; i++) {
            int h = heights[i];
            while (!stack.empty() && h <= stack.back().second) {
                stack.pop_back();
            }
            if (!stack.empty()) {
                res[i] = stack.back().first;
            }
            stack.emplace_back(i, h);
        }
        return res;

    }

};

Solution s;
TEST_CASE("[84] Test case 1", "") {
    vector<int> input = {2,1,5,6,2,3};
    auto actual = s.largestRectangleArea(input);
    REQUIRE(actual == 10);
}


TEST_CASE("[84] Test case 2", "") {
    vector<int> input = {2, 4};
    auto actual = s.largestRectangleArea(input);
    REQUIRE(actual == 4);
}


TEST_CASE("[84] Test case 3", "") {
    vector<int> input = {2, 3, 4, 3};
    auto actual = s.nextLess(input);
    REQUIRE(actual == vector<int>{4, 4, 3, 4});
}

TEST_CASE("[84] Test case 4", "") {
    vector<int> input = {2, 3, 4, 3};
    auto actual = s.prevLess(input);
    REQUIRE(actual == vector<int>{-1, 0, 1, 0});
}

TEST_CASE("[84] Test case 5", "") {
    vector<int> input = {0};
    auto actual = s.largestRectangleArea(input);
    REQUIRE(actual == 0);
}

