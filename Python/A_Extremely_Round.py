li = []
for i in range(1,1000000):
    s = str(i)
    if s.count("0")==len(s)-1:
        li.append(int(s))
        
def bin(arr,target):
    arr.sort()
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left+right) // 2
        if arr[mid] <= target:
            left = mid + 1
            ans = mid
        else:
            right = mid - 1
    return ans

t = int(input())
for _ in range(t):
    n = int(input())
    print(bin(li,n)+1)