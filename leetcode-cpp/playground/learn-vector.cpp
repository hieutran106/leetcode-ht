#include <iostream>
#include <limits>

void debugInputBuffer()
{
    std::cout << "Buffer size: " << std::cin.rdbuf()->in_avail() << std::endl;
    std::cout << "Next character: " << static_cast<char>(std::cin.peek()) << std::endl;
}

int main()
{
    int x{};
    std::cin >> x;
    debugInputBuffer();
    std::cout << "x: " << x << std::endl;

    int y{};
    std::cin >> y;
    debugInputBuffer();
    std::cout << "y: " << x << std::endl;
    return 0;
}
