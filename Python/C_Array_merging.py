t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    dict1 = {}
    old_i = a[0]
    len_ = 0
    for i in range(len(a)):
        if a[i]==old_i:
            len_ +=1
        else:
            print("print" , a[i], len_)
            dict1[old_i] = max(dict1.get(old_i, 0), len_)
            len_ = 1
            old_i = a[i]
    dict1[old_i] = max(dict1.get(old_i, 0), len_)
    print(dict1)
    
    dict2 = {}
    