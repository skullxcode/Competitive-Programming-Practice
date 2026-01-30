t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = input()
    a = set(s)
    freq = {}
    odd = 0
    for i in s:
        freq[i] = freq.get(i,0)+1
    for i in a:
        if freq[i]%2==1:
            odd+=1
    if odd-k<=1 or odd == 1:
        print("YES")
    else:
        print("NO")