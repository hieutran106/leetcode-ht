#include <stdio.h>
#include "seatest/seatest.h"
#include "solution.h"

void test_case_1()
{
    int input[] = {1, 2, 1};
    int returnSize;
    int *actual = getConcatenation(input, 3, &returnSize);

    int expect[] = {1, 2, 1, 1, 2, 1};
    assert_n_array_equal(expect, actual, 6);
}

void test_case_2()
{
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