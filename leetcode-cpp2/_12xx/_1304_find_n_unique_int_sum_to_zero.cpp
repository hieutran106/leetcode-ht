
#include <catch2/catch_test_macros.hpp>
#include <set>
#include <numeric>

// Date: 2025-09-07
// Problem: 1304 find_n_unique_int_sum_to_zero
using std::vector;
using std::string;
using std::set;

class Solution {
public:
    vector<int> sumZero(int n) {
        vector<int> ans;
        for (int i = n; i > static_cast<int>(std::ceil(n * 1.f/ 2)); i--) {
            ans.push_back(i);
            ans.push_back(-i);
        }
        if (n % 2 == 1) {
            ans.push_back(0);
        }
        return ans;
    }
};

Solution s;
TEST_CASE("[1304] Test case 1", "") {
    auto actual = s.sumZero(5);
    set<int> s(actual.begin(), actual.end());
    long long sum = std::accumulate(s.begin(), s.end(), 0LL);
    REQUIRE(s.size() == 5);
    REQUIRE(sum == 0);
}


TEST_CASE("[1304] Test case 2", "") {
    auto actual = s.sumZero(3);
    set<int> s(actual.begin(), actual.end());
    long long sum = std::accumulate(s.begin(), s.end(), 0LL);
    REQUIRE(s.size() == 3);
    REQUIRE(sum == 0);
}

TEST_CASE("[1304] Test case 3", "") {
    auto actual = s.sumZero(1);
    set<int> s(actual.begin(), actual.end());
    long long sum = std::accumulate(s.begin(), s.end(), 0LL);
    REQUIRE(s.size() == 1);
    REQUIRE(sum == 0);
}

TEST_CASE("[1304] Test case 4", "") {
    auto actual = s.sumZero(4);
    set<int> s(actual.begin(), actual.end());
    long long sum = std::accumulate(s.begin(), s.end(), 0LL);
    REQUIRE(s.size() == 4);
    REQUIRE(sum == 0);
}

