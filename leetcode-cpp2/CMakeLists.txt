cmake_minimum_required(VERSION 3.15)

include(FetchContent)
FetchContent_Declare(
        catch2
        GIT_REPOSITORY https://github.com/catchorg/Catch2.git
        GIT_TAG v3.4.0
)
FetchContent_MakeAvailable(catch2)

# Pull in Catch2's CTest integration helper
#include(Catch)

add_subdirectory(_0xx)