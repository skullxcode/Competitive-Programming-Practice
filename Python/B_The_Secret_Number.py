t = int(input())
for _ in range(t):
    n = int(input())
    arr = []
    i = 1
    while (10**i + 1)<= n:
        if n%(10**i + 1)==0:
            arr.append(n//(10**i + 1))
        i+=1
    print(len(arr))
    if arr:
        print(*sorted(arr))




# #include <bits/stdc++.h>
# using namespace std;

# int main(){
#     int t;
#     cin >> t;
#     while(t--){
#         vector<int> res;
#         int n;
#         cin >> n;
#         int i = 1;
#         while(pow(10,i)+1<n){
#             if(n%(long(pow(10,i)+1)==0)){
#                 res.push_back(n/(long(pow(10,i))+1));
#             }
#             i++;
#         }
#         sort(res.begin(), res.end());
#         cout << res.size();
#         if(res.size()!=0){
#             for(int i=0;i<res.size();++i){
#                 cout << res[i] << " ";
#             }cout << endl;
#         }
#     }
#     return 0;
# }