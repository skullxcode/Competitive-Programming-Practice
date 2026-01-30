t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    if sorted(arr)==arr:
        print(0)
    elif arr[0]==n and arr[-1]==1:
        print(3)
    elif arr[0]==1 or arr[-1]==n:
        print(1)
    else:
        print(2)