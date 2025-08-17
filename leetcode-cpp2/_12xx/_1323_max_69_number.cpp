
#include <catch2/catch_test_macros.hpp>

// Date: 2025-17-08
class Solution {
public:
    int maximum69Number (int num) {
        std::string nums = std::to_string(num);
        for (std::size_t i =0; i < nums.size(); i++) {
            if (nums[i] == '6') {
                nums[i] = '9';
                break;
            }
        }
        int ans = std::stoi(nums);
        return ans;
    }
};

TEST_CASE("Test case 1", "") {
    Solution s;
    auto actual = s.maximum69Number(9669);
    REQUIRE(actual == 9969);
}


TEST_CASE("Test case 2", "") {
    Solution s;
    auto actual = s.maximum69Number(9996);
    REQUIRE(actual == 9999);
}

TEST_CASE("Test case 3", "") {
    Solution s;
    auto actual = s.maximum69Number(9999);
    REQUIRE(actual == 9999);
}

