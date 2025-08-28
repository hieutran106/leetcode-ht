#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <catch2/catch_test_macros.hpp>

using std::vector;

vector<vector<int>> parseMatrix(const std::string& s) {
    vector<std::vector<int>> result;
    vector<int> currentRow;
    std::string number;

    for (char ch : s) {
        if (std::isdigit(ch) || ch == '-') {
            number += ch;   // accumulate digits (handles multi-digit and negative)
        }
        else if (!number.empty()) {
            currentRow.push_back(std::stoi(number));
            number.clear();
        }

        if (ch == ']') {
            if (!currentRow.empty()) {
                result.push_back(currentRow);
                currentRow.clear();
            }
        }
    }

    return result;
}

vector<int> parseVector(const std::string& s) {
    vector<int> result;
    std::string number;

    for (char ch : s) {
        if (std::isdigit(static_cast<unsigned char>(ch)) || ch == '-') {
            number += ch; // accumulate digits (supports multi-digit and negatives)
        } else {
            if (!number.empty()) {
                result.push_back(std::stoi(number));
                number.clear();
            }
        }
    }

    // Capture any trailing number if present
    if (!number.empty()) {
        result.push_back(std::stoi(number));
    }

    return result;

}


TEST_CASE("test parseMatrix", "") {
    std::string input = "[[1,2,3],[4,5,6],[7,8,9]]";
    std::vector<std::vector<int>> parsed = parseMatrix(input);

    std::vector<std::vector<int>> expect = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    REQUIRE(parsed == expect);
}

TEST_CASE("[parseVector] Test case 1", "") {
    std::string input = "[3,5,2,-6]";
    auto actual = parseVector(input);

    vector<int> expect = {3, 5, 2, -6};
    REQUIRE(actual == expect);
}

TEST_CASE("[parseVector] Test case 2", "") {
    std::string input = "[]";
    auto actual = parseVector(input);

    vector<int> expect = {};
    REQUIRE(actual == expect);
}