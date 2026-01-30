#include <bits/stdc++.h>
using namespace std;

int n;

int seq(int n){
    if(n==1){
        return 1;
    }
    if(n%2==1){
        return 1+seq(3*n+1);
    }else{
        return 1+seq(n/2);
    }
}

int main(){
    cin >> n;
    cout << seq(n) << endl;
}