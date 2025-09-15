#include <catch2/catch_test_macros.hpp>
#include "../utils/serde.cpp"
#include <bitset>
#include <set>

// Date: 2025-09-12
// Problem: 1733 min_people_to_teach
using std::vector;
using std::string;
using std::bitset;

class Solution {
public:
    int minimumTeachings(int n, vector<vector<int>>& languages, vector<vector<int>>& friendships) {
        int m = static_cast<int>(languages.size()); // number of user
        vector<std::bitset<501>> users;
        for (auto& user: languages) {
            bitset<501> userLanguages;
            for (auto l: user) {
                userLanguages.set(l);
            }
            users.push_back(userLanguages);
        }
        std::set<int> needToTeach;
        for (auto& f: friendships) {
            int u = f[0] - 1;
            int v = f[1] - 1;
            if ((users[u] & users[v]) == 0) {
                needToTeach.insert(u);
                needToTeach.insert(v);
            }
        }

        return 0;
    }
};

Solution s;
TEST_CASE("[1733] Test case 1", "") {
    auto languages = parseMatrix("[[1],[2],[1,2]]");
    auto friendships = parseMatrix("[[1,2],[1,3],[2,3]]");
    auto actual = s.minimumTeachings(2, languages, friendships);
    REQUIRE(actual == 1);
}


TEST_CASE("[1733] Test case 2", "") {
    auto languages = parseMatrix("[[2],[1,3],[1,2],[3]]");
    auto friendships = parseMatrix("[[1,4],[1,2],[3,4],[2,3]]");
    auto actual = s.minimumTeachings(3, languages, friendships);
    REQUIRE(actual == 2);
}

TEST_CASE("[1733] Test case 4", "") {
    auto languages = parseMatrix("[[3, 11, 5, 10, 1, 4, 9, 7, 2, 8, 6], [5, 10, 6, 4, 8, 7], [6, 11, 7, 9],\
                                              [11, 10, 4], [6, 2, 8, 4, 3], [9, 2, 8, 4, 6, 1, 5, 7, 3, 10],\
                                              [7, 5, 11, 1, 3, 4], [3, 4, 11, 10, 6, 2, 1, 7, 5, 8, 9],\
                                              [8, 6, 10, 2, 3, 1, 11, 5], [5, 11, 6, 4, 2]]");
    auto friendships = parseMatrix("[[7, 9], [3, 7], [3, 4], [2, 9], [1, 8], [5, 9], [8, 9], [6, 9], [3, 5],\
                                                [4, 5], [4, 9], [3, 6], [1, 7], [1, 3], [2, 8], [2, 6], [5, 7], [4, 6],\
                                                [5, 8], [5, 6], [2, 7], [4, 8], [3, 8], [6, 8], [2, 5], [1, 4], [1, 9],\
                                                [1, 6], [6, 7]]");
    auto actual = s.minimumTeachings(11, languages, friendships);
    REQUIRE(actual == 0);
}

TEST_CASE("[1733] Test case 5", "") {
    auto languages = parseMatrix("[[4, 7, 2, 14, 6], [15, 13, 6, 3, 2, 7, 10, 8, 12, 4, 9], [16], [10],\
                                              [10, 3], [4, 12, 8, 1, 16, 5, 15, 17, 13],\
                                              [4, 13, 15, 8, 17, 3, 6, 14, 5, 10],\
                                              [11, 4, 13, 8, 3, 14, 5, 7, 15, 6, 9, 17, 2, 16, 12], [4, 14, 6],\
                                              [16, 17, 9, 3, 11, 14, 10, 12, 1, 8, 13, 4, 5, 6], [14], [7, 14],\
                                              [17, 15, 10, 3, 2, 12, 16, 14, 1, 7, 9, 6, 4]]");
    auto friendships = parseMatrix("[[4, 11], [3, 5], [7, 10], [10, 12], [5, 7], [4, 5], [3, 8], [1, 5],\
                                                [1, 6], [7, 8], [4, 12], [2, 4], [8, 9], [3, 10], [4, 7], [5, 12],\
                                                [4, 9], [1, 4], [2, 8], [1, 2], [3, 4], [5, 10], [2, 7], [1, 7], [1, 8],\
                                                [8, 10], [1, 9], [1, 10], [6, 7], [3, 7], [8, 12], [7, 9], [9, 11],\
                                                [2, 5], [2, 3]]");
    auto actual = s.minimumTeachings(17, languages, friendships);
    REQUIRE(actual == 4);
}

