#include <stdio.h>
#include "seatest/seatest.h"
#include "solution.h"

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