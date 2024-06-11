#include <stdio.h>
#include "../../../deps/Unity/src/unity.h"

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** insert(int** intervals, int intervalsSize, int* intervalsColSize, int* newInterval, int newIntervalSize, int* returnSize, int** returnColumnSizes) {
    
}

void setUp(void)
{
    // set stuff up here
}

void tearDown(void)
{
    // clean stuff up here
}

void test_case_1() {
    int arr1[][2] = {{1, 3}, {6, 9}};
    int newInterval = {2, 5};
    
    TEST_ASSERT_EQUAL_INT(4, 4);
}

void test_case_2() {
    TEST_ASSERT_EQUAL_INT(5, 5);
}

int main(int argc, char **argv)
{
    UNITY_BEGIN();
    RUN_TEST(test_case_1);
    RUN_TEST(test_case_2);
    return UNITY_END();
}