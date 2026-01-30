def binary(a):
    d = ""
    while a>0:
        d +=str(a%2)
        a//=2
    d = d[::-1]
    return(d)

def decimal(a):
    b = 0
    l = len(a)
    for i in range(l):
        b += int(a[i])*(2**i)
    return(b)


t = int(input())
for _ in range(t):
    n = int(input())
    t = binary(n).count("1")
    m = "1"*t
    print(decimal(m))