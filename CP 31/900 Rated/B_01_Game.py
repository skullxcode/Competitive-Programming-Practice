t = int(input())
for _ in range(t):
    s = input()
    s0 = s.count("0")
    s1 = s.count("1")
    pair = min(s1,s0)
    if pair%2==0:
        print("NET")
    else:
        print("DA")