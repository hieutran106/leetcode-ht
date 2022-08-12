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
    int actual = balancedStringSplit("RLRRLLRLRL");
    TEST_ASSERT_EQUAL(4, actual);
}

void test_case_2() {
    int actual = balancedStringSplit("RLRRRLLRLL");
    TEST_ASSERT_EQUAL(2, actual);
}

void test_case_3() {
    int actual = balancedStringSplit("LLLLRRRR");
    TEST_ASSERT_EQUAL(1, actual);
}

int main(int argc, char **argv)
{
    UNITY_BEGIN();
    RUN_TEST(test_case_1);
    RUN_TEST(test_case_2);
    RUN_TEST(test_case_3);
    return UNITY_END();
}