#include <bits/stdc++.h>
using namespace std;



vector<int> arr;

int res(int i,int s,int x,int n){
    if(s==x && i == n){
        return 1;
    }
    if(i == n){
        return 0;
    }
    return res(i+1,s+arr[i],x,n)+res(i+1,s-arr[i],x,n);
}


int main(){
    int n,x;
    cin >> n >> x;
    int input;
    for(int i=0;i<n;++i){
        cin >> input;
        arr.push_back(input);
    }
    if(res(1,arr[0],x,n)){
        cout << "YES" << endl;
    }else{
        cout << "NO" << endl;
    }
    return 0;
}