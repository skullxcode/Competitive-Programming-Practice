#include <bits/stdc++.h>
using namespace std;

int main(){
    int t;
    cin >> t;
    while (t-->0){
        int x,y,z;
        cin >> x >> y >> z;
        if (((x&y)==(y&z))&&((x&z)==(x&y))){
            cout << "YES" << endl;
        }
        else{
            cout << "NO" << endl;
        }
    }
    return 0;
}
