
#include <catch2/catch_test_macros.hpp>

// Date: 2025-22-08
using std::vector;

class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        return 0;
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

