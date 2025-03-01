#include "../test/htcatch.h"

int add(int a, int b)
{
    return a + b;
}

TEST(test_case_1)
{
    ASSERT_EQUAL(4, 4);
    ASSERT_EQUAL(0, add(-1, 1));
}
TEST(test_case_2)
{
    ASSERT_TRUE(add(1, 1) < 0);
}

TEST(test_case_3)
{
    ASSERT_EQUAL(4, 4);
    ASSERT_EQUAL(0, add(-1, 1));
}

TEST_MAIN()