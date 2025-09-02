#include <catch2/catch_test_macros.hpp>
#include <catch2/matchers/catch_matchers_floating_point.hpp>
#include "../utils/serde.cpp"
#include <queue>
#include <tuple>

// Date: 2025-09-02
// Problem: 1792 max_average_pass_ratio
using namespace std;

class Solution {
public:
    double maxAverageRatio(vector<vector<int> > &classes, int extraStudents) {
        priority_queue<tuple<double, int, int> > heap; // Max heap
        for (auto &c: classes) {
            int p = c[0];
            int t = c[1];
            double delta = (p + 1.0) / (t + 1.0) - 1.0 * p / t;
            heap.emplace(delta, p, t);
        }
        while (extraStudents > 0) {
            auto [_, p, t] = heap.top();
            heap.pop();
            double delta = (p + 2.0) / (t + 2.0) - (p + 1.0) / (t + 1.0);
            heap.emplace(delta, p + 1, t + 1);
            extraStudents--;
        }
        double ans = 0;
        while (!heap.empty()) {
            auto [_, p, t] = heap.top();
            ans += 1.0 * p / t;
            heap.pop();
        }

        return ans / classes.size();
    }
};

Solution s;
TEST_CASE("[1792] Test case 1", "") {
    auto input = parseMatrix("[[1,2],[3,5],[2,2]]");
    auto actual = s.maxAverageRatio(input, 2);
    REQUIRE_THAT(actual, Catch::Matchers::WithinAbs(0.78333, 1e-5));
}


TEST_CASE("[1792] Test case 2", "") {
    auto input = parseMatrix("[[2,4],[3,9],[4,5],[2,10]]");
    auto actual = s.maxAverageRatio(input, 4);
    REQUIRE_THAT(actual, Catch::Matchers::WithinAbs(0.53485, 1e-5));
}

TEST_CASE("[1792] Test case 3", "") {
    auto input = parseMatrix("[[1,2],[3,5]]");
    auto actual = s.maxAverageRatio(input, 1);
    REQUIRE_THAT(actual, Catch::Matchers::WithinAbs(0.6333333333333333, 1e-10));
}
