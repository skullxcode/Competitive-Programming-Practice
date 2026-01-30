#include <bits/stdc++.h>
using namespace std;


int main() {
    double t,n,a,b;
    cin >> t;
    while(t--){
        cin >> n >> a >> b;
        double input,cntA,cntB;
        cntA = 0;
        cntB = 0;
        for(int i=0;i<n;i++){
            cin >> input;
            if(input==a){
                cntA++;
            }if(input==b){
                cntB++;
            }
        }
        cout << fixed << setprecision(10) << (cntA*cntB)/(n*n) << endl;
    }
    return 0;
}