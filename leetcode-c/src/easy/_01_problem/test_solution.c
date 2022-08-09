#include <stdio.h>
#include "seatest/seatest.h"
#include "solution.h"

void test_hello_world()
{
    char *s = "hello world!";
    assert_string_equal("hello world!", s);
    assert_string_contains("hello", s);
    assert_string_doesnt_contain("goodbye", s);
    assert_string_ends_with("!", s);
    assert_string_starts_with("hell", s);
}

void test_hello_world2()
{
    assert_int_equal(4, 4);
    float result = my_solution();
    assert_float_equal(100, result, 0.01);
}

void test_case_1() {
    assert_int_equal(4, 4);
}

void test_case_2() {
    assert_int_equal(5, 5);
}

void all_tests(void)
{
    run_test(test_case_1);
    run_test(test_case_2);
}

int main(int argc, char **argv)
{
    return run_tests(all_tests);
}