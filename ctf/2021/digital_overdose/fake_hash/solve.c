#include <iostream>
#include <string>
#include <random>
#include <cassert>  
using namespace std;

int l(int k) {
    int e = k;
    for (int i = 0; i < rand() % 1000 + 2; i++) {
        e = (e % 2) ? (((e + 1) / 2) * e) : ((e / 2) * (e + 1));
    }
    return e;
}

vector<int> outs;

void rands(int n) {
    srand(1);
    while (n--) {
        int t = rand();
    }
}

int main() {

    string chars = "abcdefghijklmnopqrstuvwxyz_0123456789";
    outs = {12253725, 20024956, 20024956, 10399080, 750925, 22247785, 10399080, 24650731, 879801, 21487290, 27243271, 10399080, 12253725, 692076, 692076, 17325441};
    string ans = "";

    int n = outs.size();
    int nrands = 0;

    for (int idx = ans.size(); idx < n; idx++) {
        bool found = false;
        while (1) {
            for (char ch : chars) {
                rands(nrands);
                int c = l(ch);
                if (c == outs[idx]) {
                    ans += ch;
                    found = true;
                    break;
                }
            }
            if (found) {
                break;
            }
            nrands++;
        }
        cout << ans << endl;
    }
}