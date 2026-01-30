n = int(input())
a = list(map(int,input().split()))
b = [abs(x) for x in a]
print(min(b))