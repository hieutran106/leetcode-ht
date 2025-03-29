#include "../test/catch_amalgamated.hpp"
#include <cmath>

using namespace std;

class Solution
{
public:
    bool checkPowersOfThree(int n)
    {
        int p = (int)floor(log10(n) / log10(3));

        return backtrack(0, 0, p, n);
    }
    bool backtrack(int curr_sum, int i, int p, int n)
    {
        if (curr_sum == n)
            return true;
        if (curr_sum > n || i > p)
            return false;
        if (backtrack(curr_sum + (int)pow(3, i), i + 1, p, n) == true)
        {
            return true;
        }

        return backtrack(curr_sum, i + 1, p, n);
    }
};

TEST_CASE("test_case_1")
{
    Solution s;
    auto actual = s.checkPowersOfThree(20597);
    CHECK(actual == false);
}

TEST_CASE("test_case_2")
{
    Solution s;
    auto actual = s.checkPowersOfThree(30493);
    CHECK(actual == false);
}

TEST_CASE("test_case_3")
{
    Solution s;
    auto actual = s.checkPowersOfThree(91);
    CHECK(actual == true);
}

TEST_CASE("test_case_4")
{
    Solution s;
    auto actual = s.checkPowersOfThree(12);
    CHECK(actual == true);
}
