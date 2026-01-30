def build(idx,l,r):
    if l==r:
        tree[idx] = arr[l]
        return
    
    mid = l + (r-l)//2
    
    build(2*idx+1,l,mid)
    build(2*idx+2,mid+1,r)
    
    tree[idx] = (tree[2*idx+1]+tree[2*idx+2])
    return


def query(idx,l,r,ql,qr):
    if r<ql or l>qr:
        return 0
    
    if ql<=l and qr>=r:
        return tree[idx]
    
    mid = l + (r-l)//2
    
    return (query(2*idx+1,l,mid,ql,qr)+query(2*idx+2,mid+1,r,ql,qr))

def update(idx,l,r,qidx,qval):
    if l==r:
        tree[idx] = qval
        return
    
    mid = l + (r-l)//2
    
    if qidx<=mid:
        update(2*idx+1,l,mid,qidx,qval)
    else:
        update(2*idx+2,mid+1,r,qidx,qval)
    
    tree[idx] = (tree[2*idx+1]+tree[2*idx+2])

n,q = map(int,input().split())
arr = list(map(int,input().split()))
tree = [0]*(4*n)
build(0,0,n-1)
for _ in range(q):
    l,r = map(int,input().split())
    print(query(0,0,n-1,l-1,r-1))