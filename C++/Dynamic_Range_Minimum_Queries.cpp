#include <bits/stdc++.h>
using namespace std;

vector<long> arr;
vector<long> tree;
void build(long idx,long l,long r){
    if(l==r){
        tree[idx] = arr[l];
        return;
    }
    long mid; 
    mid = l+(r-l)/2;
    
    build(2*idx+1,l,mid);
    build(2*idx+2,mid+1,r);

    tree[idx] = min(tree[2*idx+1],tree[2*idx+2]);
    return;
}

long query(long idx,long l,long r, long ql, long qr){
    long mid;
    if(r<ql || l>qr){
        return 1e9;
    }
    if(ql<=l && qr>=r){
        return tree[idx];
    }

    mid = l+(r-l)/2;

    return min(query(2*idx+1,l,mid,ql,qr),query(2*idx+2,mid+1,r,ql,qr));
}

void update(long idx,long l,long r, long qidx, long qval){
    long mid;
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
    long n;
    long q;
    cin >> n >> q;
    long input;
    for (long i = 0; i < n; ++i){
        cin>>input;
        arr.push_back(input);
    }
    tree.assign(4*n,0);
    build(0,0,n-1);

    while(q--){
        long k,ql,qr;
        cin >> k >> ql >> qr;
        if(k==1){
            update(0,0,n-1,ql-1,qr);
        }else{
        cout<< query(0,0,n-1,ql-1,qr-1)<<endl;
    }
    }

    return 0;
}