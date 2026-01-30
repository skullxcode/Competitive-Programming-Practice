n,m = map(int,input().split())
if n==0 and m!=0:
    print("Impossible")
else:
    if m==0 and n==0:
        min_=0
        max_=0
    elif m==0:
        min_ = n
        max_ =n
    elif n>=m:
        min_ = n
        max_ = n+m-1
    else:
        min_ = m
        max_ = n+m-1
    print(min_,max_)    