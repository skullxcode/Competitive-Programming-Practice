#include <bits/stdc++.h>
using namespace std;

void digit(int n){
    if(n==0){
        return;
    }
    digit(n-1);
    cout << "I love Recursion" << endl;
}

int main() {
    long long n;
    cin >> n;
    digit(n);
    return 0;
}