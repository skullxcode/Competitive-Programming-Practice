def build(idx,l,r):
    if l==r:
        tree[idx] = arr[l]
        return
    
    mid = l + (r-l)//2
    
    build(2*idx+1,l,mid)
    build(2*idx+2,mid+1,r)
    
    tree[idx] = max(tree[2*idx+1],tree[2*idx+2])
    return


def query(idx,l,r,ql,qr):
    if r<ql or l>qr:
        return float('-inf')
    
    if ql<=l and qr>=r:
        return tree[idx]
    
    mid = l + (r-l)//2
    
    return max(query(2*idx+1,l,mid,ql,qr),query(2*idx+2,mid+1,r,ql,qr))
    
def update(idx,l,r,qidx,qval):
    if l==r:
        tree[idx] = qval
        return
    
    mid = l + (r-l)//2
    
    if qidx<=mid:
        update(2*idx+1,l,mid,qidx,qval)
    else:
        update(2*idx+2,mid+1,r,qidx,qval)
    
    tree[idx] = max(tree[2*idx+1],tree[2*idx+2])
        
        

n = int(input())
arr = list(map(int,input().split()))
tree = [0]*(4*n)
build(0,0,n-1)
