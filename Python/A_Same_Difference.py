t = int(input())
for _ in range(t):
    l = int(input())
    s = input()
    last = s[-1]
    n = s.count(last)
    print(l-n)