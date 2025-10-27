
#include <catch2/catch_test_macros.hpp>

// Date: 2025-10-27
// Problem: 2125 number_laser_beam
using std::vector;
using std::string;

class Solution {
public:
    int numberOfBeams(vector<string>& bank) {
        int ans = 0;
        int prevCount = 0;
        for (string& row: bank) {
            int oneCount = 0;
            for (char c:row) {
                if (c == '1') oneCount++;
            }
            if (oneCount == 0) continue;
            // handle there is laser
            ans += oneCount * prevCount;
            prevCount = oneCount;
        }
        return ans;
    }
};

Solution s;
TEST_CASE("[2125] Test case 1", "") {
    vector<string> bank = {"011001","000000","010100","001000"};
    auto actual = s.numberOfBeams(bank);
    REQUIRE(actual == 8);
}


TEST_CASE("[2125] Test case 2", "") {
    vector<string> bank = {"000","111","000"};
    auto actual = s.numberOfBeams(bank);
    REQUIRE(actual == 0);
}

