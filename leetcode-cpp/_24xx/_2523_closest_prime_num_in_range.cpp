#include "../test/catch_amalgamated.hpp"

using namespace std;

class Solution
{
public:
    vector<int> closestPrimes(int left, int right)
    {
        auto primes = getPrimes(left, right);
        if (primes.size() <= 1)
        {
            return vector<int>{-1, -1};
        }
        auto ans = vector<int>{primes.at(0), primes.at(1)};
        int diff = primes.at(1) - primes.at(0);
        for (int i = 0; i < primes.size() - 1; i++)
        {
            if (primes.at(i + 1) - primes.at(i) < diff)
            {
                ans.at(0) = primes.at(i);
                ans.at(1) = primes.at(i + 1);
                diff = primes.at(i + 1) - primes.at(i);
            }
        }
        return ans;
    }

    vector<int> getPrimes(int left, int right)
    {
        vector<bool> nums(right + 1, true);
        nums.at(0) = false;
        nums.at(1) = false;
        for (int i = 2; i < (int)sqrt(right) + 1; i++)
        {
            if (nums.at(i) == false)
            {
                continue;
            }
            for (int j = i + i; j < right + 1; j = j + i)
            {
                nums.at(j) = false;
            }
        }

        vector<int> primes{};
        for (size_t i = 0; i < right + 1; i++)
        {
            if (nums.at(i) == true && i >= left && i <= right)
            {
                primes.push_back(i);
            }
        }
        return primes;
    }
};

TEST_CASE("test_case_1")
{
    Solution s;
    auto actual = s.closestPrimes(10, 19);
    auto expect = vector<int>{11, 13};
    CHECK(actual == expect);
}

TEST_CASE("test_case_2")
{
    Solution s;
    auto actual = s.closestPrimes(4, 6);
    auto expect = vector<int>{-1, -1};
    CHECK(actual == expect);
}

TEST_CASE("test_case_3")
{
    Solution s;
    auto actual = s.closestPrimes(1, 1);
    auto expect = vector<int>{-1, -1};
    CHECK(actual == expect);
}

TEST_CASE("test_case_4")
{
    Solution s;
    auto actual = s.closestPrimes(1, 1000000);
    auto expect = vector<int>{2, 3};
    CHECK(actual == expect);
}
