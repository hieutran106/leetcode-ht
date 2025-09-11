cmake_minimum_required(VERSION 3.15)
project(leetcode-ht-cpp2)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)


include(FetchContent)
FetchContent_Declare(
        catch2
        GIT_REPOSITORY https://github.com/catchorg/Catch2.git
        GIT_TAG v3.4.0
)
FetchContent_MakeAvailable(catch2)

# Pull in Catch2's CTest integration helper
#include(Catch)
add_subdirectory(playground)
add_subdirectory(utils)
add_subdirectory(_0xx)
add_subdirectory(_2xx)
add_subdirectory(_22xx)
add_subdirectory(_10xx)
add_subdirectory(_12xx)
add_subdirectory(_14xx)
add_subdirectory(_30xx)
add_subdirectory(_4xx)
add_subdirectory(_16xx)
add_subdirectory(_26xx)
