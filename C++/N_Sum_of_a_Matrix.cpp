#include <bits/stdc++.h>
using namespace std;

int r,c;
vector<vector<int>> a,b;


void gridSum(int i, int j){
    if(i==r-1 && j==c-1){
        a[i][j]+=b[i][j];
        return;
    }
    if(j==c-1){
        a[i][j]+=b[i][j];
        return gridSum(i+1,0);
    }else{
        a[i][j]+=b[i][j];
        return gridSum(i,j+1);
    }
}

int main(){
    cin >> r >> c;
    for(int i=0;i<r;i++){
        vector<int> arr;
        for(int j = 0;j<c;j++){
            int input;
            cin >> input;
            arr.push_back(input);
        }
        a.push_back(arr);
    }
    for(int i=0;i<r;i++){
        vector<int> arr;
        for(int j = 0;j<c;j++){
            int input;
            cin >> input;
            arr.push_back(input);
        }
        b.push_back(arr);
    }
    gridSum(0,0);
    for(int i=0;i<r;i++){
        for(int j = 0;j<c;j++){
            cout << a[i][j] << " ";
        }
        cout << endl;
    }
}