#include <bits/stdc++.h>
using namespace std;

int n;
vector<int> arr;

double avg(int i,double s){
    if(i==n){
        return s;
    }
    return avg(i+1,s+arr[i]);
}

int main(){
    cin >> n;
    int i = n;
    while(i--){
        int input;
        cin >> input;
        arr.push_back(input);
    }
    cout << fixed << setprecision(6) << avg(0,0)/n << endl;
    return 0;
}