t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    max_sum = -1
    i = 1
    while i*i<=b:
        if b%i==0:
            k = i
            a1 = a*k
            b1 = b//k
            s1 = a1+b1
            if s1%2==0:
                max_sum = max(max_sum,s1)
                
                
            l = b//i
            a2 = a*l
            b2 = b//l
            s2 = a2+b2
            if s2%2==0:
                max_sum = max(max_sum,s2)
        i+=1
    print(max_sum)