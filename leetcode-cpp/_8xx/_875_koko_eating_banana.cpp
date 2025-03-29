#include "../test/catch_amalgamated.hpp"
#include <algorithm>

using namespace std;

class Solution
{
public:
    int minEatingSpeed(vector<int> &piles, int h)
    {
        int l{1};
        int r = *std::max_element(piles.begin(), piles.end());
        while (l <= r)
        {
            auto mid = (r + l) / 2;
            auto canEat = this->canEat(mid, piles, h);
            if (canEat)
            {
                // koko can eat within h hour, we need to find from l -> mid
                r = mid - 1;
            }
            else
            {
                // koko cannot finish, need to eat at faster speed
                l = mid + 1;
            }
        }
        return l;
    }

    bool canEat(int speed, vector<int> &piles, int h)
    {
        int actualHour{0};
        for (auto banana : piles)
        {
            // substitute std::ceil(static_cast<double>(banana) / speed) with (banana - 1)/speed + 1
            // Faster than using ceil() with doubles
            actualHour = actualHour + (banana - 1) / speed + 1;
            if (actualHour > h)
                return false;
        }
        return true;
    }
};

TEST_CASE("test_case_1")
{
    Solution s;
    auto piles = vector<int>{3, 6, 7, 11};
    auto actual = s.minEatingSpeed(piles, 8);
    CHECK(actual == 4);
}

TEST_CASE("test_case_2")
{
    Solution s;
    auto piles = vector<int>{30, 11, 23, 4, 20};
    auto actual = s.minEatingSpeed(piles, 5);
    CHECK(actual == 30);
}

TEST_CASE("test_case_3")
{
    Solution s;
    auto piles = vector<int>{30, 11, 23, 4, 20};
    auto actual = s.minEatingSpeed(piles, 6);
    CHECK(actual == 23);
}
