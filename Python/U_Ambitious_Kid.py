n = int(input())
a = list(map(int,input().split()))
b = [abs(number) for number in a]
b.sort()
print(b[0])