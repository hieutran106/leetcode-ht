#include <stdio.h>
#include "unity/unity.h"
#include "solution.h"
#include <string.h>

void setUp(void)
{
    // set stuff up here
}

void tearDown(void)
{
    // clean stuff up here
}

void test_case_1() {
    char s[] = "codeleet";
    int indices[] = {4,5,6,7,0,2,1,3};
    char *actual = restoreString(s, indices, strlen(s));
    TEST_ASSERT_EQUAL_STRING(actual, "leetcode");
}

void test_case_2() {
    char s[] = "abc";
    int indices[] = {0,1,2};
    char *actual = restoreString(s, indices, strlen(s));
    TEST_ASSERT_EQUAL_STRING(actual, "abc");
}

int main(int argc, char **argv)
{
    UNITY_BEGIN();
    RUN_TEST(test_case_1);
    RUN_TEST(test_case_2);
    return UNITY_END();
}