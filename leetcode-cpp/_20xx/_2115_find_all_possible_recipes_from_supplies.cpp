#include <iostream>
#include <unordered_map>
#include <unordered_set>

#include "../test/catch_amalgamated.hpp"

using namespace std;

class Solution {
   public:
    vector<string> findAllRecipes(vector<string> &recipes,
                                  vector<vector<string>> &ingredients,
                                  vector<string> &supplies) {
        auto graph = this->buildGraph(recipes, ingredients);
        auto canCooked = unordered_set(supplies.begin(), supplies.end());
        auto visit = unordered_set<string>{};

        auto ans = vector<string>{};
        for (auto r : recipes) {
            if (this->dfs(r, graph, canCooked, visit)) {
                ans.push_back(r);
            }
        }
        return ans;
    }

    bool dfs(string r, unordered_map<string, vector<string>> graph,
             unordered_set<string> canCooked, unordered_set<string> visit) {
        if (canCooked.contains(r)) {
            return true;
        }
        if (visit.contains(r) || !graph.contains(r)) {
            return false;
        }
        visit.insert(r);
        auto neighbours = graph[r];
        for (auto ingredient : neighbours) {
            if (!this->dfs(ingredient, graph, canCooked, visit)) {
                return false;
            }
        }
        canCooked.insert(r);
        return true;
    }

    unordered_map<string, vector<string>> buildGraph(
        vector<string> &recipes, vector<vector<string>> &ingredients) {
        unordered_map<string, vector<string>> graph;
        for (size_t i = 0; i < recipes.size(); i++) {
            graph.insert(std::make_pair(recipes.at(i), ingredients.at(i)));
        }

        return graph;
    }
};

TEST_CASE("test_case_1") {
    Solution s;
    auto recipes = vector<string>{"bread"};
    auto ingredients = vector<vector<string>>{{"yeast", "flour"}};
    auto supplies = vector<string>{"yeast", "flour", "corn"};
    auto actual = s.findAllRecipes(recipes, ingredients, supplies);
    auto expect = vector<string>{"bread"};

    CHECK(actual == expect);
}

TEST_CASE("test_case_2") {
    Solution s;
    auto recipes = vector<string>{"bread", "sandwich"};
    auto ingredients =
        vector<vector<string>>{{"yeast", "flour"}, {"bread", "meat"}};
    auto supplies = vector<string>{"yeast", "flour", "meat"};
    auto actual = s.findAllRecipes(recipes, ingredients, supplies);
    auto expect = vector<string>{"bread", "sandwich"};
    CHECK(actual == expect);
}

TEST_CASE("test_case_3") {
    Solution s;
    auto recipes = vector<string>{"bread", "sandwich", "burger"};
    auto ingredients = vector<vector<string>>{
        {"yeast", "flour"}, {"bread", "meat"}, {"sandwich", "meat", "bread"}};
    auto supplies = vector<string>{"yeast", "flour", "meat"};
    auto actual = s.findAllRecipes(recipes, ingredients, supplies);
    auto expect = vector<string>{"bread", "sandwich", "burger"};
    CHECK(actual == expect);
}

TEST_CASE("test_case_5") {
    Solution s;
    auto recipes = vector<string>{"ju", "fzjnm", "x", "e", "zpmcz", "h", "q"};
    auto ingredients = vector<vector<string>>{
        {"d"},
        {"hveml", "f", "cpivl"},
        {"cpivl", "zpmcz", "h", "e", "fzjnm", "ju"},
        {"cpivl", "hveml", "zpmcz", "ju", "h"},
        {"h", "fzjnm", "e", "q", "x"},
        {"d", "hveml", "cpivl", "q", "zpmcz", "ju", "e", "x"},
        {"f", "hveml", "cpivl"}};
    auto supplies = vector<string>{"f", "hveml", "cpivl", "d"};
    auto actual = s.findAllRecipes(recipes, ingredients, supplies);
    auto expect = vector<string>{"ju", "fzjnm", "q"};
    CHECK(actual == expect);
}

TEST_CASE("test_case_6") {
    Solution s;
    auto recipes = vector<string>{"burger", "bread", "sandwich"};
    auto ingredients = vector<vector<string>>{
        {"sandwich", "meat", "bread"}, {"yeast", "flour"}, {"bread", "meat"}};
    auto supplies = vector<string>{"yeast", "flour", "meat"};
    auto actual = s.findAllRecipes(recipes, ingredients, supplies);
    auto expect = vector<string>{"burger", "bread", "sandwich"};
    CHECK(actual == expect);
}
