
#include <catch2/catch_test_macros.hpp>
#include "../utils/serde.cpp"
#include <format>
// Date: 2025-08-29
// Problem: 321 create_maximum_number
using std::vector;
using std::string;

class Solution {
public:
    vector<int> maxNumber(vector<int>& nums1, vector<int>& nums2, int k) {
        vector<int> ans(k, 0);
        for (int i = 0; i <= k ;i++) {
            if (i > nums1.size() || k - i > nums2.size()) {
                continue;
            }
            auto n1 = maxNumberHelper(nums1, i);
            auto n2 = maxNumberHelper(nums2, k - i);
            auto c = merge(n1, n2);
            string log = std::format("n1={}, n2={}, c={}", formatVec(n1), formatVec(n2), formatVec(c));
            std::cout << log << std::endl;
            printVec(c);
            if (isGreater(c, ans, 0, 0)) {
                ans = c;
            }
        }
        return ans;
    }

    vector<int> maxNumberHelper(vector<int>& nums, int k) {
        // Create the maximum number of length k
        // using decreasing stack
        int removeCount = nums.size() - k;
        vector<int> stack;
        for (auto& n: nums) {
            while (!stack.empty() && n > stack.back() && removeCount > 0) {
                stack.pop_back();
                removeCount--;
            }
            stack.push_back(n);
        }
        // take the first k element from stack
        vector<int> ans(stack.begin(), stack.begin() + k);
        return ans;
    }

    vector<int> merge(vector<int>& nums1, vector<int>& nums2) {
        // Merge two integers to form a max number
        vector<int> ans;
        size_t i = 0, j = 0;
        while (i < nums1.size() && j < nums2.size()) {
            if (nums1[i] == nums2[j]) {
                if (isGreater(nums1, nums2, i+1, j +1 )) {
                    ans.push_back(nums1[i]);
                    i++;
                } else {
                    ans.push_back(nums2[j]);
                    j++;
                }
            } else
            if (nums1[i] > nums2[j]) {
                ans.push_back(nums1[i]);
                i++;
            } else {
                ans.push_back(nums2[j]);
                j++;
            }
        }
        while (i < nums1.size()) {
            ans.push_back(nums1[i]);
            i++;
        }

        while (j < nums2.size()) {
            ans.push_back(nums2[j]);
            j++;
        }
        return ans;
    }

    bool isGreater(vector<int>& nums1, vector<int>& nums2, int i, int j) {
        int n = static_cast<int>(nums1.size());
        int m = static_cast<int>(nums2.size());
        while (i < n && j < m && nums1[i] == nums2[j]) {
            i++;
            j++;
        }
        if (j == m) return true;   // nums2 exhausted => nums1 is greater or equal
        if (i == n) return false;  // nums1 exhausted while nums2 remains
        return nums1[i] > nums2[j];


    }

};

Solution s;
TEST_CASE("[321] Test case 01", "") {
    auto nums1 = parseVector("3,4,6,5");
    auto nums2 = parseVector("9,1,2,5,8,3");
    auto actual = s.maxNumber(nums1, nums2, 5);
    auto expect = parseVector("9,8,6,5,3");
    REQUIRE(actual == expect);
}


TEST_CASE("[321] Test case 02", "") {
    auto nums1 = parseVector("6,7");
    auto nums2 = parseVector("6,0,4");
    auto actual = s.maxNumber(nums1, nums2, 5);
    auto expect = parseVector("6,7,6,0,4");
    REQUIRE(actual == expect);
}

TEST_CASE("[321] Test case 03", "") {
    auto nums1 = parseVector("3,9");
    auto nums2 = parseVector("8,9");
    auto actual = s.maxNumber(nums1, nums2, 3);
    auto expect = parseVector("9,8,9");
    REQUIRE(actual == expect);
}

TEST_CASE("[321] Test case 04", "") {
    auto nums1 = parseVector("0,0,0");
    auto nums2 = parseVector("8,9");
    auto actual = s.maxNumber(nums1, nums2, 1);
    auto expect = parseVector("9");
    REQUIRE(actual == expect);
}

TEST_CASE("[321] Test case 05", "") {
    auto nums = parseVector("9,1,2,5,8,3");
    auto actual = s.maxNumberHelper(nums, 3);
    auto expect = parseVector("9,8,3");
    REQUIRE(actual == expect);
}


TEST_CASE("[321] Test case 06", "") {
    auto nums1 = parseVector("6, 5");
    auto nums2 = parseVector("9, 8, 3");
    auto actual = s.merge(nums1, nums2);
    auto expect = parseVector("9, 8, 6, 5, 3");
    REQUIRE(actual == expect);
}

TEST_CASE("[321] Test case 07", "") {
    auto nums1 = parseVector("9,8,3");
    auto nums2 = parseVector("6,5");
    auto actual = s.merge(nums1, nums2);
    auto expect = parseVector("9, 8, 6, 5, 3");
    REQUIRE(actual == expect);
}


TEST_CASE("[321] Test case 08", "") {
    auto nums1 = parseVector("9,1,2,5,8,3");
    auto nums2 = parseVector("3,4,6,5");
    auto actual = s.maxNumber(nums1, nums2, 5);
    auto expect = parseVector("9,8,6,5,3");
    REQUIRE(actual == expect);
}

TEST_CASE("[321] Test case 09", "") {
    auto nums1 = parseVector("2,5,6,4,4,0");
    auto nums2 = parseVector("7,3,8,0,6,5,7,6,2");
    auto actual = s.maxNumber(nums1, nums2, 15);
    auto expect = parseVector("7,3,8,2,5,6,4,4,0,6,5,7,6,2,0");
    REQUIRE(actual == expect);
}

TEST_CASE("[321] Test case 10", "") {
    auto nums1 = parseVector("4");
    auto nums2 = parseVector("4,6,5");
    auto actual = s.merge(nums1, nums2);
    auto expect = parseVector("4,6,5,4");
    REQUIRE(actual == expect);
}

TEST_CASE("[321] Test case 11", "") {
    auto nums1 = parseVector("2,2");
    auto nums2 = parseVector("2,3");
    auto actual = s.merge(nums1, nums2);
    auto expect = parseVector("2,3,2,2");

    vector<int> x= {6, 5};
    vector<int> y = {6};

    REQUIRE(actual == expect);
}

