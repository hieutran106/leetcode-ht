#include "unity/unity.h"
#include "solution.h"

void setUp(void) {
    // set stuff up here
}

void tearDown(void) {
    // clean stuff up here
}

void test_case_1()
{
    char *input[] = {
        "alice and bob love leetcode",
        "i think so too",
        "this is great thanks very much"};
    int actual = mostWordsFound(input, 3);
    TEST_ASSERT_EQUAL_INT(6, actual);
}

void test_case_2()
{
    char *input[] = {
        "please wait",
        "continue to fight",
        "continue to win"};
    int actual = mostWordsFound(input, 3);
    TEST_ASSERT_EQUAL_INT(3, actual);
}

// not needed when using generate_test_runner.rb
int main(void) {
    UNITY_BEGIN();
    RUN_TEST(test_case_1);
    RUN_TEST(test_case_2);
    return UNITY_END();
}