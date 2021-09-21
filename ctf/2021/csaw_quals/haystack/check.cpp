#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(int argc, char* argv[]) {
    time_t t = time(0);
    int off = atoi(argv[1]);
    srand(t + off);
    printf("%d\n", rand() % 0x100000);
    srand(t + off + 1);
    printf("%d\n", rand() % 0x100000);
    srand(t + off + 2);
    printf("%d\n", rand() % 0x100000);
    return 0;
}