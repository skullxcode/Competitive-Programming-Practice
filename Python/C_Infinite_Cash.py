s = int(input(),2)
d = int(input(),2)
m = int(input(),2)
   
def count(n):
    cnt = 0
    while n>0:
        n = n//2
        cnt+=1
    return cnt

if count(m)<d:
    print(bin(count(m))[2::])
elif count(s)>=d:
    print("Infinite money!")
else:
    day = 0
    while m>0:
        m = m//2
        day+=1
        if day==d:
            break
    k = m+s
    i = 0
    while k>0:
        k = k//2
        i+=1
        if i%d==0:
            k+=s
        if k==0:
            break
    print(bin(i+day)[2::])