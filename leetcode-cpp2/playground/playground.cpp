#include <cstdio>
#include <cstdlib>
#include <cstring>

int main() {
    char *buff = (char *) malloc(20);
    strcpy(buff, "Hello world");
    free(buff);
    printf("%s\n", buff); // Use-after-free!
    return 0;
}