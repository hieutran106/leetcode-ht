#include <unordered_map>

#include "../test/catch_amalgamated.hpp"
using namespace std;

class Solution {
   public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        unordered_map<int, int> map;
        for (size_t i = 0; i < nums.size(); i++) {
            auto num = nums[i];
            if (map.contains(num) && i - map[num] <= k) {
                return true;
            }
            map[num] = i;
        }
        return false;
    }
};

TEST_CASE("test_case_1") {
    Solution s;
    auto nums = vector<int>{1, 2, 3, 1};
    auto actual = s.containsNearbyDuplicate(nums, 3);
    CHECK(actual == true);
}

TEST_CASE("test_case_2") {
    Solution s;
    auto nums = vector<int>{1, 0, 1, 1};
    auto actual = s.containsNearbyDuplicate(nums, 1);
    CHECK(actual == true);
}

TEST_CASE("test_case_3") {
    Solution s;
    auto nums = vector<int>{1, 2, 3, 1, 2, 3};
    auto actual = s.containsNearbyDuplicate(nums, 2);
    CHECK(actual == false);
}
