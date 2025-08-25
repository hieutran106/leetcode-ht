add_executable(serde serde.cpp)
target_link_libraries(serde PRIVATE Catch2::Catch2WithMain)