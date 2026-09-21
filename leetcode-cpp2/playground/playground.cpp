#include <iostream>

int main() {
    std::cout << "Hello, World!" << std::endl;
    int** handle{nullptr};
    handle = new int*;

    *handle = new int{42};

    int value = *(*handle);
    auto x = sizeof(handle);
    auto y = sizeof(*handle);
    auto z = sizeof(*(*handle));

    int* u = *handle;
    int* v = &(*(*handle));

    // cleanup
    delete *handle;
    delete handle;
    return 0;
}