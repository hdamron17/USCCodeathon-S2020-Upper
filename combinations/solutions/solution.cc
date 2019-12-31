#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
// Int scores 65.71
// Long scores 97.14 with segfault on 0 case


int main() {
    int n, k;
    cin >> n >> k;
    int l[k];
    for (int i = 0; i < k; ++i) {
        cin >> l[i];
    }
    
    int count[k][n+1];
    for (int i = 0; i < k; ++i) {
        for (int j = 0; j < n+1; ++j) {
            count[i][j] = 0;
        }
    }
    for (int i = 0; i < k; ++i) count[i][0] = 1;
    for (int i = 0; i < n+1; i += l[0]) count[0][i] = 1;
    
    for (int i = 1; i < k; ++i) {
        for (int j = 1; j < n+1; ++j) {
            int useJ = j - l[i];
            int x = (useJ < 0) ? 0 : count[i][useJ];
            count[i][j] = count[i-1][j] + x;
        }
    }
    cout << count[k-1][n] << endl;
    return 0;
}

