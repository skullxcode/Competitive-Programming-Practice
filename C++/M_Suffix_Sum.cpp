#include <bits/stdc++.h>
using namespace std;

int n,m;
vector<long long> arr;

long long arrSum(int i){
    if(i == n-m-1){
        return 0;
    }
    return arr[i] + arrSum(i-1);
}

int main(){
    cin >> n >> m;
    arr.resize(n);
    for(int i = 0; i < n; i++){
        cin >> arr[i];
    }
    cout << arrSum(n-1) << endl;
    return 0;
}