// #include <bits/stdc++.h>
// using namespace std;


// int main() {
//     int t,n,a,b;
//     cin >> t;
//     while(t--){
//         cin >> n >> a >> b;
//         if(abs(a-b)!=1 && abs(a-b)!=2){
//             cout << 0 << endl;
//         }
//         else{
//             if(abs(a-b)==2 || a==1 || a==n || b==1 || b==n){
//                 cout << 1 << endl;
//             }else{
//                 cout << 2 << endl;
//             }
//         }
//     }
//     return 0;
// }


#include <bits/stdc++.h>
using namespace std;

// unordered_map<int,int> frq;

vector<int> h;

int main(){
    int n,q;
    h.resize(10*10*10*10*10+1);
    cin >> n >> q;
    while(n--){
        int input;
        cin >> input; 
        h[input]+=1;
    }
    while(q--){
        int query;
        cin >> query;
        cout << h[query] << endl;
    }
}