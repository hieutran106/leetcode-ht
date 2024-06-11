#include <stdio.h>
#include <stdlib.h>
#include "../../../deps/Unity/src/unity.h"

int *sorted(int *array, int length)
{
    // create new array
    int *ret = malloc(sizeof(int) * length);
    for (int i = 0; i < length; i++)
    {
        ret[i] = array[i];
    }
    // sort in-place
    int temp;
    for (int i = 0; i < length; i++)
    {
        for (int j = 0; j < length - 1; j++)
        {
            if (ret[j] > ret[j + 1])
            {
                temp = ret[j];
                ret[j] = ret[j + 1];
                ret[j + 1] = temp;
            }
        }
    }
    return ret;
}

int heightChecker(int *heights, int heightsSize)
{
    int res = 0;
    int *sortedHeights = sorted(heights, heightsSize);
    for (int i = 0; i < heightsSize; i++)
    {
        if (sortedHeights[i] != heights[i])
        {
            res++;
        }
    }
    return res;
}

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
    int heights[] = {1, 1, 4, 2, 1, 3};
    int actual = heightChecker(heights, 6);
    TEST_ASSERT_EQUAL_INT(3, actual);
}

void test_case_2()
{
    int heights[] = {5, 1, 2, 3, 4};
    int actual = heightChecker(heights, 5);
    TEST_ASSERT_EQUAL_INT(5, actual);
}

void test_case_3()
{
    int heights[] = {1, 2, 3, 4, 5};
    int actual = heightChecker(heights, 5);
    TEST_ASSERT_EQUAL_INT(0, actual);
}

int main(int argc, char **argv)
{
    UNITY_BEGIN();
    RUN_TEST(test_case_1);
    RUN_TEST(test_case_2);
    RUN_TEST(test_case_3);
    return UNITY_END();
}