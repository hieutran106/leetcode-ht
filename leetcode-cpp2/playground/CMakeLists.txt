message(STATUS "C++ compiler: ${CMAKE_CXX_COMPILER}")
message(STATUS "C++ compiler ID: ${CMAKE_CXX_COMPILER_ID}")
message(STATUS "C++ compiler version: ${CMAKE_CXX_COMPILER_VERSION}")

include(CheckCXXCompilerFlag)
check_cxx_compiler_flag("-std=c++20" HAS_CXX20)

if (HAS_CXX20)
    set(CMAKE_CXX_STANDARD 20)
    message(STATUS "C++ compiler support c++20")
endif()


add_executable(playground playground.cpp)
target_link_libraries(playground PRIVATE Catch2::Catch2WithMain)