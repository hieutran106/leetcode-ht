#include <stdio.h>
#include "unity/unity.h"
#include "solution.h"

void setUp(void)
{
    // set stuff up here
}

void tearDown(void)
{
    // clean stuff up here
}

void test_case_1() {
    assert_int_equal(4, 4);
}

void test_case_2() {
    assert_int_equal(5, 5);
}

int main(int argc, char **argv)
{
    UNITY_BEGIN();
    RUN_TEST(test_case_1);
    RUN_TEST(test_case_2);
    return UNITY_END();
}