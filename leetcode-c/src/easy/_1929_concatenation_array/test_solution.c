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