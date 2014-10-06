
#include <stdio.h>

int main() {
    int t, i, j;
    scanf("%d", &t);
    for (i = 1; i <= t / 2; ++i) {
        for (j = i + 1; j <= (t + 1) / 2; ++j) {
            if ((i + j) * (j - i + 1) / 2  == t && (i + j) * (j - i + 1) % 2 == 0) {
                printf("%d\n", i);
            }
        }
    }

    return 0;
}
