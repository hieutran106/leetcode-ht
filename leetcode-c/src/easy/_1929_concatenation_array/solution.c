#include <stdlib.h>
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
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