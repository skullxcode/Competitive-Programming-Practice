#include <bits/stdc++.h>
using namespace std;

int res(int s,int e){
    if(s>e){
        return 0;
    }if(s==e){
        return 1;
    }
    return res(s+1,e) + res(s+2,e) + res(s+3,e);
}

int main(){
    int s,e;
    cin >> s >> e;
    cout << res(s,e) << endl;
    return 0;
}