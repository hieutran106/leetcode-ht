#ifndef SIMPLE_TEST_H
#define SIMPLE_TEST_H

#include <iostream>
#include <limits>
#include <vector>
#include <functional>
#include <string>
#include <stdexcept>

class AssertionFailedException : public std::runtime_error
{
public:
    AssertionFailedException(const std::string &message) : std::runtime_error(message) {}
};

#define ASSERT_TRUE(condition)                                                                                 \
    do                                                                                                         \
    {                                                                                                          \
        if (!(condition))                                                                                      \
        {                                                                                                      \
            throw AssertionFailedException(std::string("Assertion failed: ") + #condition + " is not true\n" + \
                                           "File: " + __FILE__ + ", Line: " + std::to_string(__LINE__));       \
        }                                                                                                      \
    } while (0)

#define ASSERT_EQUAL(expected, actual)                                                                               \
    do                                                                                                               \
    {                                                                                                                \
        if ((expected) != (actual))                                                                                  \
        {                                                                                                            \
            throw AssertionFailedException(std::string("Assertion failed: ") + #expected + " != " + #actual + "\n" + \
                                           "Expected: " + std::to_string(expected) + "\n" +                          \
                                           "Actual: " + std::to_string(actual) + "\n" +                              \
                                           "File: " + __FILE__ + ", Line: " + std::to_string(__LINE__));             \
        }                                                                                                            \
    } while (0)

class TestSuite
{
private:
    std::vector<std::pair<std::string, std::function<void()>>> tests;

public:
    void add_test(const std::string &name, std::function<void()> test)
    {
        tests.push_back(std::make_pair(name, test));
    }

    void run()
    {
        int passed = 0;
        long unsigned int total = tests.size();

        for (const auto &test : tests)
        {
            std::cout << "Running test: " << test.first << "... ";
            try
            {
                test.second();
                std::cout << "PASSED\n";
                passed++;
            }
            catch (const AssertionFailedException &e)
            {
                std::cout << "FAILED\n";
                std::cerr << e.what() << "\n";
            }
            catch (const std::exception &e)
            {
                std::cout << "FAILED (Unexpected exception)\n";
                std::cerr << "Error: " << e.what() << "\n";
            }
            catch (...)
            {
                std::cout << "FAILED (Unknown exception)\n";
            }
        }

        std::cout << "\nTest summary:\n";
        std::cout << passed << " out of " << total << " tests passed.\n";
    }
};

TestSuite &get_test_suite()
{
    static TestSuite instance;
    return instance;
}

#define TEST(name)                                                     \
    void name();                                                       \
    struct name##_registrar                                            \
    {                                                                  \
        name##_registrar() { get_test_suite().add_test(#name, name); } \
    } name##_reg;                                                      \
    void name()

#define TEST_MAIN()                            \
    int main()                                 \
    {                                          \
        std::cout << __cplusplus << std::endl; \
        get_test_suite().run();                \
        return 0;                              \
    }

#endif // SIMPLE_TEST_H
