#include <iostream>
#include <vector>
#include <string>
#include <sstream>

using std::vector;

vector<vector<int>> parseNestedVector(const std::string& s) {
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

// Example usage
int main() {
    std::string input = "[[1,2,3],[4,5,6],[7,8,9]]";
    std::vector<std::vector<int>> parsed = parseNestedVector(input);

    for (const auto& row : parsed) {
        for (int val : row)
            std::cout << val << " ";
        std::cout << "\n";
    }
}