#include <algorithm>
#include <iostream>

#include "../test/catch_amalgamated.hpp"
using namespace std;

class Solution {
   public:
    int countDays(int days, vector<vector<int>>& meetings) {
        int x = 1;
        std::sort(meetings.begin(), meetings.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[0] < b[0];
        });
        // merge the meetings
        vector<vector<int>> merged{};
        for (auto meeting : meetings) {
            if (merged.size() == 0) {
                merged.push_back(meeting);
                continue;
            }
            auto& last = merged.back();
            if (last[1] < meeting[0]) {
                merged.push_back(meeting);
            } else {
                last[1] = std::max(last[1], meeting[1]);
            }
        }
        int meeting_count = 0;
        for (auto meeting : merged) {
            meeting_count += meeting[1] - meeting[0] + 1;
        }

        return days - meeting_count;
    }
};

TEST_CASE("test_case_1") {
    Solution s;
    auto meetings = vector<vector<int>>{{5, 7}, {1, 3}, {9, 10}};
    auto actual = s.countDays(10, meetings);
    CHECK(actual == 2);
}

TEST_CASE("test_case_2") {
    Solution s;
    auto meetings = vector<vector<int>>{{2, 4}, {1, 3}};
    auto actual = s.countDays(5, meetings);
    CHECK(actual == 1);
}

TEST_CASE("test_case_3") {
    Solution s;
    auto meetings = vector<vector<int>>{{1, 6}};
    auto actual = s.countDays(6, meetings);
    CHECK(actual == 0);
}
