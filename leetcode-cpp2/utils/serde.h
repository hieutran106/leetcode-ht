#pragma once

#include <vector>
#include <string>

std::vector<std::vector<int>> parseMatrix(const std::string& s);

std::vector<int> parseVector(const std::string& s);
void printVec(const std::vector<int>& v);
std::string formatVec(const std::vector<int>& v);