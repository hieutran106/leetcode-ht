#include <stdbool.h>
#include "../../../deps/Unity/src/unity.h"

#define MAX_SIZE 10000

typedef struct Stack {
    char arr[MAX_SIZE];
    int top;
} Stack;
void stack_initialize(Stack *stack);
bool isEmpty(Stack *stack);
void push(Stack *stack, char value);
char pop(Stack *stack);
char peek(Stack *stack);


void stack_initialize(Stack *stack) {
    stack->top = -1;
}

bool isEmpty(Stack *stack) {
    return stack->top == -1;
}

void push(Stack *stack, char value) {
    stack->top++;
    stack->arr[stack->top] = value;
}

char pop(Stack *stack) {
    if (stack->top == -1) {
        return '\0';
    }
    char value = stack->arr[stack->top];
    stack->top --;
    return value;
}

char peek(Stack *stack) {
    if (stack->top == -1) {
        return '\0';
    }
    return stack->arr[stack->top];
}
bool isPair(char c1, char c2) {
    if (c1 == '(' && c2 ==')') return true;
    if (c1 == '{' && c2 =='}') return true;
    if (c1 == '[' && c2 ==']') return true;
    return false;
}
bool isValid(char* s) {
    Stack stack;
    stack_initialize(&stack);
    while (*s != '\0') {
        if (*s == '{' || *s == '(' || *s == '[') {
            push(&stack, *s);
            s++;
            continue;
        } 
        // Pop element at the top of stack
        char atPeek = peek(&stack);
        if (isPair(atPeek, *s)) {
            pop(&stack);
            s++;
        } else {
            return false;
        }

    }

    bool res = isEmpty(&stack);
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

void test_case_1() {
    bool actual = isValid("(]");
    TEST_ASSERT_FALSE(actual);
}

void test_case_2() {
    bool actual = isValid("()");
    TEST_ASSERT_TRUE(actual);
}

void test_case_3() {
    bool actual = isValid("()[]{}");
    TEST_ASSERT_TRUE(actual);
}

void test_case_4() {
    bool actual = isValid("]");
    TEST_ASSERT_FALSE(actual);
}

int main(int argc, char **argv)
{
    UNITY_BEGIN();
    RUN_TEST(test_case_1);
    RUN_TEST(test_case_2);
    RUN_TEST(test_case_3);
    RUN_TEST(test_case_4);
    return UNITY_END();
}