a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))
d = list(map(int,input().split()))
e = list(map(int,input().split()))
count = 0
if 1 in a:
    k = a.index(1)
    if k == 0 or k == 4:
        count+=4
    elif k == 1 or k == 3:
        count+=3
    else:
        count+=2
elif 1 in e:
    k = e.index(1)
    if k == 0 or k == 4:
        count+=4
    elif k == 1 or k == 3:
        count+=3
    else:
        count+=2
    
elif 1 in b:
    k = b.index(1)
    if k == 0 or k == 4:
        count+=3
    elif k == 1 or k == 3:
        count+=2
    else:
        count+=1
elif 1 in d:
    k = d.index(1)
    if k == 0 or k == 4:
        count+=3
    elif k == 1 or k == 3:
        count+=2
    else:
        count+=1
else:
    k = c.index(1)
    if k == 0 or k == 4:
        count+=2
    elif k == 1 or k == 3:
        count+=1
    else:
        count+=0
print(count)