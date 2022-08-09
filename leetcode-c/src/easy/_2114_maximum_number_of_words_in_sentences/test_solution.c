#include <stdio.h>
#include "seatest/seatest.h"
#include "solution.h"

void test_case_1()
{
    char *input[] = {
        "alice and bob love leetcode",
        "i think so too",
        "this is great thanks very much"};
    int actual = mostWordsFound(input, 3);
    assert_int_equal(6, actual);
}

void test_case_2()
{
    char *input[] = {
        "please wait",
        "continue to fight",
        "continue to win"};
    int actual = mostWordsFound(input, 3);
    assert_int_equal(3, actual);
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