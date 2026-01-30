t = int(input())
for _ in range(t):
    h,d = map(int,input().split())
    count = 0
    distance=0
    i = 1
    while distance<d:
            if h-i>0:
                h = h - i
                i += 1
                count+=1
                distance+=1
            else:
                h += 1
                i = 1
                count+=1
    print(count)