#include<stdio.h>
#include<stdlib.h>
#include<time.h>

int main(void) {
    unsigned long x = time(0);
    srand((unsigned int)(((x >> 8) & 0xffffff) << 8));

    for (int it = 0; it < 2; it++) {
        int n = 0;
        int r = rand();
        for(int y = r; y; y /= 10) {
            n += (y % 10);
        }
        printf("%d %d\n", n, r);
    }
}