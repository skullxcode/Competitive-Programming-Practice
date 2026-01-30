#include <bits/stdc++.h>
using namespace std;

int n,w;
vector<int> weight,value;


int res(int i,int rw){
    if(i==n || rw==0){
        return 0;
    }
    if(weight[i]<=rw){
        return max(value[i]+res(i+1,rw-weight[i]),res(i+1,rw));
    }else{
        return max(0,res(i+1,rw));
    }
}


int main(){
    cin >> n >> w;
    int i = n;
    while(i--){
        int w1,v1;
        cin >> w1 >> v1;
        weight.push_back(w1);
        value.push_back(v1);
    }
    cout << res(0,w) << endl;
    return 0;
}