#include <bits/stdc++.h>
using namespace std;
using ll = long long;

ll n;

int lo(ll n){
    if(n<=1){
        return 0;
    }
    return 1+lo(n/2);
}

int main(){
    cin >> n;
    cout << lo(n) << endl;
}