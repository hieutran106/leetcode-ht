#include "../test/catch_amalgamated.hpp"
#include <iostream>

using namespace std;

class Solution
{
public:
    int minimumRecolors(string blocks, int k)
    {
        int count{0};
        for (int i = 0; i < k; i++)
        {
            if (blocks.at(i) == 'W')
                count += 1;
        }
        int ans = count;
        // Another way to count correctly
        int c1 = count_if(blocks.begin(), blocks.begin() + k, [](char c)
                          { return c == 'W'; });
        for (int i = 1; i < blocks.size() - k + 1; i++)
        {
            if (blocks.at(i - 1) == 'W')
            {
                count -= 1;
            }
            if (blocks.at(i + k - 1) == 'W')
            {
                count += 1;
            }
            ans = min(count, ans);
            if (count < ans)
            {
                ans = count;
                std::cout << "Found min at " << i << " count:" << count << endl;
            }
        }
        return ans;
    }
};

TEST_CASE("test_case_1")
{
    Solution s;
    auto actual = s.minimumRecolors("WBBWWBBWBW", 7);
    CHECK(actual == 3);
}

TEST_CASE("test_case_2")
{
    Solution s;
    auto actual = s.minimumRecolors("WBWBBBW", 2);
    CHECK(actual == 0);
}

TEST_CASE("test_case_3")
{
    Solution s;
    auto actual = s.minimumRecolors("B", 1);
    CHECK(actual == 0);
}

TEST_CASE("test_case_4")
{
    Solution s;
    auto actual = s.minimumRecolors("W", 1);
    CHECK(actual == 1);
}

TEST_CASE("test_case_5")
{
    Solution s;
    auto actual = s.minimumRecolors("WWBBBWBBBBBWWBWWWB", 16);
    CAPTURE(actual);
    CHECK(actual == 6);
}
