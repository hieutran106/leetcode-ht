add_executable(playground playground.cpp)
target_link_options(playground PRIVATE -fsanitize=address)
target_compile_options(playground PRIVATE -fsanitize=address)