#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> grid;

long res(int i,int j,int s,int n,int m){
    if(i>=n || j>=m){
        return -10e9;
    }
    if(i==n-1 && j==m-1){
        return grid[i][j];
    }
    return grid[i][j] + max(res(i+1,j,s+grid[i][j],n,m),res(i,j+1,s+grid[i][j],n,m));
}

int main(){
    int n,m;
    cin >> n >> m;
    int input;
    for(int i=0;i<n;++i){
        vector<int> row;
        for(int j=0;j<m;++j){
            cin >> input;
            row.push_back(input);
        }
        grid.push_back(row);
    }
    cout << res(0,0,0,n,m) << endl;
    return 0;
}


#include <bits/stdc++.h>
using namespace std;

// --- Type Definitions ---
using ll = long long;
using pii = pair<int, int>;
using pll = pair<ll, ll>;
using vi = vector<int>;
using vll = vector<ll>;

// --- Macros ---
#define pb push_back
#define mp make_pair
#define all(x) (x).begin(), (x).end()
#define rall(x) (x).rbegin(), (x).rend()
#define sz(x) (int)(x).size()
#define rep(i, a, b) for (int i = a; i < b; ++i)
#define per(i, a, b) for (int i = b - 1; i >= a; --i)
#define f first
#define s second

// --- Constants ---
const int INF = 1e9;
const ll MOD = 1e9 + 7;

// --- Solution Function ---
void solve() {
    
}

// --- Main Function ---
int main() {
    // Fast I/O
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t = 1;
    cin >> t;
    while (t--) {
        solve();
    }

    return 0;
}
