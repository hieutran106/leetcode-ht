#include <iostream>
#include <vector>
#include <string>

int main()
{
    // Create a vector of strings
    std::vector<std::string> fruits;

    // Add elements to the vector
    fruits.push_back("Apple");
    fruits.push_back("Banana");
    fruits.push_back("Orange");
    fruits.push_back("Mango");

    // Print the size of the vector
    std::cout << "Number of fruits: " << fruits.size() << std::endl;

    // Print all elements using a range-based for loop
    std::cout << "Fruits in the vector:" << std::endl;
    for (const auto &fruit : fruits)
    {
        std::cout << fruit << std::endl;
    }

    // Access and modify an element
    fruits[1] = "Grape";

    // Print the modified vector
    std::cout << "\nAfter modification:" << std::endl;
    for (size_t i = 0; i < fruits.size(); ++i)
    {
        std::cout << i << ": " << fruits[i] << std::endl;
    }

    return 0;
}
