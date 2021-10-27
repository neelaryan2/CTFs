#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(int argc, char* argv[]) {
	time_t v3 = time(0LL);
    int off = atoi(argv[1]);
	srand(v3 + off);
	int v8 = 0;
	for (int i = 1; i <= 300; ++i) {
		if (i % 6) {
			v8 += rand() % 7;
		} else {
			printf("%d ", v8);
			v8 = 0;
			v8 = rand() % 7;
		}
	}
}