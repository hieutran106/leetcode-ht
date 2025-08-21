// #include <string>
// #include <vector>
#include <iostream>

using namespace std; // using-directive: pulls in everything from std

class Item {
public:
    Item() : value{12} {
        std::cout << "Item constructor 1" << endl;
    }

    explicit Item(int v) : value{v} {
        std::cout << "Item constructor 2" << endl;
    }

    int value;
};

class Meter {
public:
    explicit Meter(double v) : value{v} {
        age = 2;
        item = Item{4};
        std::cout << "Meter constructor" << endl;
    }



    Item item;
    double value;
    int age;
};


void print(Meter m) {
    m.item.value = 16;
}

int main() {
    Meter m{14.f};
    print(m);
    std::cout << m.item.value << endl;
}
