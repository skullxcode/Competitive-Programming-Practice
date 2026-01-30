#include <bits/stdc++.h>
using namespace std;

void digit(int n){
    if (n==1){
        cout << 1;
        return;
    }
    cout << n << " ";
    digit(n-1);
}

int main() {
    long long n;
    cin >> n;
    digit(n);
    return 0;
}