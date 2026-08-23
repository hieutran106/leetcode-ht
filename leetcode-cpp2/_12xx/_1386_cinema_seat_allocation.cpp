#include "serde.h"
#include <catch2/catch_test_macros.hpp>

// Date: 2026-08-23
// Problem: 1386 cinema_seat_allocation
using std::string;
using std::vector;

class Solution
{
public:
	int maxNumberOfFamilies(int n, vector<vector<int>> & reservedSeats)
	{
		std::unordered_map<int, std::bitset<10>> c;
		for(const auto & item : reservedSeats)
		{
			const auto row = item[0];
			const auto seat = item[1];
			if(!c.contains(row))
			{
				c[row] = std::bitset<10>();
			}
			c[row].set(seat - 1);
		}
		int ans = 0;
		for(const auto & [row, seats] : c)
		{
			std::bitset<8> line((seats >> 1).to_ulong() & 0xFF);
			std::bitset<4> left((seats >> 1).to_ulong() & 0x0F);
			std::bitset<4> mid((seats >> 3).to_ulong() & 0x0F);
			std::bitset<4> right((seats >> 5).to_ulong() & 0x0F);
			if(line == 0)
			{
				ans += 2;
			}
			else if(left == 0 || mid == 0 || right == 0)
			{
				ans += 1;
			}
		}
		ans += (n - c.size()) * 2;
		return ans;
	}
};

Solution s;
TEST_CASE("[1386] Test case 1", "")
{
	auto reservedSeats = vector<vector<int>>{
		{1, 2 },
        {1, 3 },
        {1, 8 },
        {2, 6 },
        {3, 1 },
        {3, 10}
	};
	auto actual = s.maxNumberOfFamilies(3, reservedSeats);
	REQUIRE(actual == 4);
}

TEST_CASE("[1386] Test case 2", "")
{
	auto reservedSeats = parseMatrix("[[2,1],[1,8],[2,6]]");
	auto actual = s.maxNumberOfFamilies(2, reservedSeats);
	REQUIRE(actual == 2);
}

TEST_CASE("[1386] Test case 3", "")
{
	auto reservedSeats = parseMatrix("[[4,3],[1,4],[4,6],[1,7]]");
	auto actual = s.maxNumberOfFamilies(4, reservedSeats);
	REQUIRE(actual == 4);
}
