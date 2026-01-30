n = int(input())
for _ in range(n):
    a = input()
    l = len(a)
    if l >10:
        k = a[0]+str(l-2)+a[-1]
        print(k)
    else:
        print(a)