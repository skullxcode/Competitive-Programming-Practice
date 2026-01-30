#include <bits/stdc++.h>
using namespace std;

int n;
vector<int> arr;

void res(int i,int ma){
    if(i>n-1){
        return;
    }
    if(ma>arr[i]){
        cout << ma << " ";
        res(i+1,ma);
    }else{
        cout << arr[i] << " ";
        res(i+1,arr[i]);
    }
}

int main(){
    cin >> n;
    int i = n;
    while(i--){
        int input;
        cin >> input;
        arr.push_back(input);
    }
    res(0,LONG_MIN);
    return 0;
}