cmake_minimum_required(VERSION 3.15)
project(leetcode-ht-cpp2)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)


include(FetchContent)
FetchContent_Declare(
        Catch2
        GIT_REPOSITORY https://github.com/catchorg/Catch2.git
        GIT_TAG v3.15.3
)
FetchContent_MakeAvailable(Catch2)

include(CTest)
include(Catch)

# Utils library (shared across all targets)
add_library(utils STATIC utils/serde.cpp)
target_include_directories(utils PUBLIC ${CMAKE_SOURCE_DIR}/utils)

# Create a separate target for each .cpp file in _* folders
file(GLOB_RECURSE TEST_SOURCES CONFIGURE_DEPENDS "${CMAKE_SOURCE_DIR}/_*/*.cpp")
foreach(SOURCE_FILE ${TEST_SOURCES})
    get_filename_component(TARGET_NAME ${SOURCE_FILE} NAME_WE)
    add_executable(${TARGET_NAME} ${SOURCE_FILE})
    target_link_libraries(${TARGET_NAME} PRIVATE Catch2::Catch2WithMain utils)
    catch_discover_tests(${TARGET_NAME})
endforeach()
