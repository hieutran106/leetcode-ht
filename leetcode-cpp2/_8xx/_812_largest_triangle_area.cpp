#include <catch2/catch_test_macros.hpp>
#include <catch2/matchers/catch_matchers_floating_point.hpp>
#include "../utils/serde.cpp"

// Date: 2025-09-27
// Problem: 812 largest_triangle_area
using std::vector;
using std::string;

double calcArea(int x1, int y1, int x2, int y2, int x3, int y3) {
    auto t = std::abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2));
    return 1.0 * t / 2;
}

class Solution {
public:
    double largestTriangleArea(vector<vector<int> > &points) {
        double ans = 0;
        for (auto i = 0; i < points.size() - 2; i++) {
            for (auto j = i + 1; j < points.size() - 1; j++) {
                for (auto k = j + 1; k < points.size(); k++) {
                    ans = std::max(ans, calcArea(points[i][0], points[i][1], points[j][0], points[j][1], points[k][0],
                                                 points[k][1]));
                }
            }
        }
        return ans;
    }
};

Solution s;
TEST_CASE("[812] Test case 1", "") {
    auto points = parseMatrix("[[0,0],[0,1],[1,0],[0,2],[2,0]]");
    auto actual = s.largestTriangleArea(points);
    REQUIRE_THAT(actual, Catch::Matchers::WithinRel(2.0, 1e-5));
}


TEST_CASE("[812] Test case 2", "") {
    auto points = parseMatrix("[[1,0],[0,0],[0,1]]");
    auto actual = s.largestTriangleArea(points);
    REQUIRE_THAT(actual, Catch::Matchers::WithinRel(0.5, 1e-5));
}
