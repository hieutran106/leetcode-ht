#include <stdio.h>
#include "unity/unity.h"
#include "solution.h"
#include <stdbool.h>

void setUp(void)
{
    // set stuff up here
}

void tearDown(void)
{
    // clean stuff up here
}

void test_case_1()
{
    int candies[] = {2, 3, 5, 1, 3};
    int returnSize = 0;
    bool *actual = kidsWithCandies(candies, 5, 3, &returnSize);
    bool expect[] = {true, true, true, false, true};
    for (int i = 0; i < returnSize; i ++) {
        printf("%d\n", actual[i]);
        TEST_ASSERT_EQUAL(expect[i], actual[i]);
    }
}


int main(int argc, char **argv)
{
    UNITY_BEGIN();
    RUN_TEST(test_case_1);
    // RUN_TEST(test_case_2);
    return UNITY_END();
}