#include <stdlib.h>
#include "../../../deps/Unity/src/unity.h"

int *getConcatenation(int *nums, int numsSize, int *returnSize)
{
    int* result = (int*)malloc(sizeof(int) * numsSize * 2);
    for (int i = 0; i < numsSize; i++)
    {
        result[i] = *(nums + i);
        result[i + numsSize] = *(nums + i);
    }

    *returnSize = numsSize * 2;
    return result;
}

void setUp(void) {
    // set stuff up here
}

void tearDown(void) {
    // clean stuff up here
}

void test_case_1()
{
    int input[] = {1, 2, 1};
    int returnSize;
    int *actual = getConcatenation(input, 3, &returnSize);

    int expect[] = {1, 2, 1, 1, 2, 1};
    TEST_ASSERT_EQUAL_INT_ARRAY(expect, actual, 6);
}

// not needed when using generate_test_runner.rb
int main(void) {
    UNITY_BEGIN();
    RUN_TEST(test_case_1);
    return UNITY_END();
}