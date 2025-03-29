#include "../test/catch_amalgamated.hpp"

using namespace std;

class Solution
{
public:
    bool isPowerOfThree(int n)
    {
        if (n < 1)
        {
            return false;
        }
        while (n > 1)
        {
            auto r = n % 3;
            if (r != 0)
            {
                return false;
            }
            n = n / 3;
        }
        return true;
    }
};

TEST_CASE("test_case_1")
{
    Solution s;
    auto actual = s.isPowerOfThree(27);
    CHECK(actual == true);
}

TEST_CASE("test_case_2")
{
    Solution s;
    auto actual = s.isPowerOfThree(0);
    CHECK(actual == false);
}

TEST_CASE("test_case_3")
{
    Solution s;
    auto actual = s.isPowerOfThree(-1);
    CHECK(actual == false);
}
