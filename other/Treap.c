
#include <iostream>
#include <time.h>
#include <stdlib.h>
#define MAX 100

using namespace std;

typedef struct {
    int l, r, key, fix;
} node;

class treap {
public:
    node p[MAX];
    int size, root;

    treap() {
        srand(time(0));
        size = -1;
        root = -1;
    }

    void insert(int &k, int x) {
        if (k == -1) {
            k = ++size;
            p[k].l = p[k].r = -1;
            p[k].key = x;
            p[k].fix = rand();
        } else if (x < p[k].key) {
            insert(p[k].l, x);
            if (p[p[k].l].fix > p[k].fix) {
                rotate_r(k);
            }
        } else {
            insert(p[k].r, x);
            if (p[p[k].r].fix > p[k].fix) {
                rotate_l(k);
            }
        }
    }

    void remove(int &k, int x) {
        if (k == -1) {
            return;
        }
        if (x < p[k].key) {
            remove(p[k].l, x);
        } else if (x > p[k].key) {
            remove(p[k].r, x);
        } else {
            if (p[k].l == -1 && p[k].r == -1) {
                k = -1;
            } else if (p[k].l == -1) {
                k = p[k].r;
            } else if (p[k].r == -1) {
                k = p[k].l;
            } else if (p[p[k].l].fix < p[p[k].r].fix) {
                rotate_l(k);
                remove(p[k].l, x);
            } else {
                rotate_r(k);
                remove(p[k].r, x);
            }
        }
    }

    void rotate_l(int &x) {
        int y = p[x].r;
        p[x].r = p[y].l;
        p[y].l = x;
        x = y;
    }

    void rotate_r(int &x) {
        int y = p[x].l;
        p[x].l = p[y].r;
        p[y].r = x;
        x = y;
    }
};

int main() {
    return 0;
}

            



