#include <bits/stdc++.h>
using namespace std;

int n;
vector<int> arr;

int palindrome(int l,int r){
    if(l>=r){
        return 1;
    }if(arr[l]!=arr[r]){
        return 0;
    }
    return (palindrome(l+1,r-1));
}

int main(){
    cin >> n;
    int i = n;
    while(i--){
        int input;
        cin >> input;
        arr.push_back(input);
    }
    if(palindrome(0,n-1)){
        cout << "YES" << endl;
    }else{
        cout << "NO" << endl;
    }
}