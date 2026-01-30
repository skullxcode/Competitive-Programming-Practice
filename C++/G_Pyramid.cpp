#include <bits/stdc++.h>
using namespace std;

void pyramid(int i, int n) {
    if (i == n) return;
    for (int j = 0; j < n-i-1; j++)
        cout << " ";
    for (int j = 0; j < 2*i+1; j++)
        cout << "*";
    cout << endl;
    pyramid(i + 1, n);
}

int main() {
    int n;
    cin >> n;
    pyramid(0, n);
    return 0;
}
