t = int(input())
for _ in range(t):
    n = input()
    l = len(n)
    for i in range(l):
        print(n[l-i-1],end=" ")
    print()