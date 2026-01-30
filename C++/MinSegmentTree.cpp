#include <bits/stdc++.h>
using namespace std;

vector<int> arr;
vector<int> tree;
void build(int idx,int l,int r){
    if(l==r){
        tree[idx] = arr[l];
        return;
    }
    int mid; 
    mid = l+(r-l)/2;
    
    build(2*idx+1,l,mid);
    build(2*idx+2,mid+1,r);

    tree[idx] = min(tree[2*idx+1],tree[2*idx+2]);
    return;
}

int query(int idx,int l,int r, int ql, int qr){
    int mid;
    if(r<ql || l>qr){
        return 1e9;
    }
    if(ql<=l && qr>=r){
        return tree[idx];
    }

    mid = l+(r-l)/2;

    return min(query(2*idx+1,l,mid,ql,qr),query(2*idx+2,mid+1,r,ql,qr));
}

void update(int idx,int l,int r, int qidx, int qval){
    int mid;
    if(l==r){
        tree[idx] = qval;
        return;
    }

    mid = l+(r-l)/2;

    if(qidx<=mid){
        update(2*idx+1,l,mid,qidx,qval);
    }else{
        update(2*idx+2,mid+1,r,qidx,qval);
    }
    tree[idx] = min(tree[2*idx+1],tree[2*idx+2]);
    return;
}

int main() {
    int n;
    int q;
    cin >> n >> q;
    int input;
    for (int i = 0; i < n; ++i){
        cin>>input;
        arr.push_back(input);
    }
    tree.assign(4*n,0);
    build(0,0,n-1);

    while(q--){
        int ql,qr;
        cin >> ql >> qr;

        cout<< query(0,0,n-1,ql,qr)<<endl;
    }

    return 0;
}