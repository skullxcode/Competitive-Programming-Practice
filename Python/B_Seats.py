t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    if n==1:
        print(1)
    else:
        arr = [x for x in s]
        for i in range(1,n-1):
            if arr[i]==arr[i-1]==arr[i+1]=="0":
                arr[i] = "1"
        print(arr.count("1"))