#include <bits/stdc++.h>
using namespace std;

void digit(int n){
    if(n==0){
        return;
    }
    digit(n/10);
    cout << n%10 << " ";
}

int main() {
    int t;
    cin >> t;
    while(t--){
        long long n;
        cin >> n;
        if(n){
        digit(n);
        cout << endl;
        }
        else{
            cout << 0 << endl;
        }
    }
    return 0;
}