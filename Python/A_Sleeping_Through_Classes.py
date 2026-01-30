t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = input()
    i = 0
    ans = 0
    awake = -1
    while i < n:
        if s[i] == "1":
            awake = i + k
            i += 1
        elif i <= awake:
            i += 1
        else:
            if s[i] == "0":
                ans += 1
            i += 1
    print(ans)
