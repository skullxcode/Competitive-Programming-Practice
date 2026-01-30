#include <bits/stdc++.h>
using namespace std;

int n,r;

long long nCr(int n,int r){
    if(r>n){
        return 0;
    }
    if(r==n || r==0){
        return 1;
    }
    return(nCr(n-1,r-1)+nCr(n-1,r));
}
int main(){
    cin >> n >> r;
    cout << nCr(n,r) << endl;
    return 0;
}