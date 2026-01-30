#include <bits/stdc++.h>
using namespace std;

int n;
vector<long long> arr;

long long arrSum(int i){
    if(i==n){
        return 0;
    }
    return arr[i] + arrSum(i+1);
}

int main(){
    cin >> n;
    arr.resize(n);
    for(int i = 0; i < n; i++){
        cin >> arr[i];
    }
    cout << arrSum(0) << endl;
    return 0;
}