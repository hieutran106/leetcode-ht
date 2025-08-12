cmake_minimum_required(VERSION 3.15)

# _191_count_1_bit test binary
add_executable(_191_count_1_bit _191_count_1_bit.cpp)
target_link_libraries(_191_count_1_bit PRIVATE Catch2::Catch2WithMain)