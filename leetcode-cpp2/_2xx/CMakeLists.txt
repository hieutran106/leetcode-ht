cmake_minimum_required(VERSION 3.15)

# _342_power_of_four test binary
add_executable(_342_power_of_four _342_power_of_four.cpp)
target_link_libraries(_342_power_of_four PRIVATE Catch2::Catch2WithMain)
