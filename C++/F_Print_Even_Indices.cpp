#include <bits/stdc++.h>
using namespace std;

int n;
vector<long long> arr;

void even(int i){
    if(i==-1){
        return;
    }
    if(i%2==0){
        cout << arr[i] << " ";
    }even(i-1);
}

int main(){
    cin >> n;
    arr.resize(n);
    for(int i = 0; i < n; i++){
        cin >> arr[i];
    }
    even(n-1);
    return 0;
}