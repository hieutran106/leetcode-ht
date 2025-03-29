#include "../test/catch_amalgamated.hpp"
#include <numeric>
#include <iostream>

using namespace std;

class Solution
{
public:
    int maximumCandies(vector<int> &candies, long long k)
    {
        auto total = std::accumulate(candies.begin(), candies.end(), 0LL);
        if (total < k)
        {
            return 0;
        }
        long long r = total / k;
        long long l{1};
        while (l <= r)
        {
            auto mid = (l + r) / 2;
            bool canAllocate = this->canAllocate(mid, candies, k);
            cout << "l=" << l << " r=" << r << " mid=" << mid << " canAllocate=" << canAllocate << endl;
            if (canAllocate)
            {
                // second half
                l = mid + 1;
            }
            else
            {
                r = mid - 1;
            }
        }
        return l - 1;
    }

    bool canAllocate(int candie, vector<int> &candies, long long k)
    {
        long long childrenCount = 0;
        for (auto n : candies)
        {
            childrenCount += n / candie;
            if (childrenCount >= k)
            {
                return true;
            }
        }
        return false;
    }
};

TEST_CASE("test_case_1")
{
    Solution s;
    auto candies = vector<int>{5, 8, 6};
    auto actual = s.maximumCandies(candies, 3);
    CHECK(actual == 5);
}

TEST_CASE("test_case_2")
{
    Solution s;
    auto candies = vector<int>{2, 5};
    auto actual = s.maximumCandies(candies, 11);
    CHECK(actual == 0);
}

TEST_CASE("test_case_3")
{
    Solution s;
    auto candies = vector<int>{1, 2, 3, 4, 10};
    auto actual = s.maximumCandies(candies, 5);
    CHECK(actual == 3);
}
