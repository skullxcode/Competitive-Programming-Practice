#include <bits/stdc++.h>

using namespace std;

int k = 0;

int ans(long long i,long long n){
    if(i==n){
        return 1;
    }
    if(i>n){
        return 0;
    }
    return ans(i*10,n) || ans(i*20,n);
}



int main(){
    int t;
    cin>>t;
    while(t--){
        long long n;
        cin >> n;
        if(ans(1,n)){
            cout << "YES" << endl;
        }else{
            cout << "NO" << endl;
        }

    }
}