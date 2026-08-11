#include "../utils/serde.h"
#include <catch2/catch_test_macros.hpp>
#include <map>
// Date: 2025-09-25
// Problem: 120 triangle
using std::string;
using std::vector;

class Solution
{
public:
	int minimumTotal(vector<vector<int>> & triangle)
	{
		std::map<std::pair<int, int>, int> memo;
		std::function<int(int, int)> dp = [&triangle, &dp, &memo](int r, int c) -> int
		{
			if(r == triangle.size() - 1)
			{
				return triangle[r][c];
			}
			std::pair key = {r, c};
			if(memo.contains(key))
			{
				return memo[{r, c}];
			}
			int down = dp(r + 1, c);
			int diag = dp(r + 1, c + 1);
			int res = triangle[r][c] + std::min(down, diag);
			memo[{r, c}] = res;
			return res;
		};

		return dp(0, 0);
	}
};

TEST_CASE("[120] Test case 1", "")
{
	Solution s;
	auto input = parseMatrix("[[2],[3,4],[6,5,7],[4,1,8,3]]");
	auto actual = s.minimumTotal(input);
	REQUIRE(actual == 11);
}

TEST_CASE("[120] Test case 2", "")
{
	Solution s;
	auto input = parseMatrix("[[-10]]");
	auto actual = s.minimumTotal(input);
	REQUIRE(actual == -10);
}

TEST_CASE("[120] Test case 3", "")
{
	Solution s;
	auto input = parseMatrix("[[1], [2, 3]");
	auto actual = s.minimumTotal(input);
	REQUIRE(actual == 3);
}
