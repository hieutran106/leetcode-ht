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
    int actual = countVowelPermutation(1);
    TEST_ASSERT_EQUAL(5, actual);
}

void test_case_2() {
    int actual = countVowelPermutation(2);
    TEST_ASSERT_EQUAL(10, actual);
}

void test_case_3() {
    int actual = countVowelPermutation(5);
    TEST_ASSERT_EQUAL(68, actual);
}

void test_case_4() {
    int actual = countVowelPermutation(144);
    TEST_ASSERT_EQUAL(18208803, actual);
}

void test_case_5() {
    int actual = countVowelPermutation(1000);
    TEST_ASSERT_EQUAL(89945857, actual);
}

int main(int argc, char **argv)
{
    UNITY_BEGIN();
    RUN_TEST(test_case_1);
    RUN_TEST(test_case_2);
    RUN_TEST(test_case_3);
    RUN_TEST(test_case_4);
    RUN_TEST(test_case_5);
    return UNITY_END();
}
