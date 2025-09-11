#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <string>


class Comp {
    std::string compName;
public:
    Comp(): compName{"UUU"} {
        int x {5};
        int y = x + 1;
    }

    std::string getCompName() {
        return compName;
    }
};


class Foo {
    int32_t age;
    std::string name;
    Comp myComp;
public:
    Foo(int a, std::string n): age{10}, name{"Ola"}, myComp{} {
        age = 20;
        myComp.getCompName();
    }
};


int main() {
    Foo f{2, "Test"};

    return 0;

}