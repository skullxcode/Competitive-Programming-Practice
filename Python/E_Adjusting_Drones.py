def binary(a,arr):
    l = 0
    r = len(arr)
    while l<=r:
        mid = (l+r)//2
        if arr[mid]<=a:
            r = mid+1
            ans = mid
        else:
            l = mid - 1
    return ans


a = [9,5,4,3,3,2,1]
print(binary(3,a))
# t = int(input())
# for _ in range(t):
#     n,k= map(int,input().split())
#     a = list(map(int,input().split()))
#     a.sort()
#     a.reverse()
#     for i in set(a):
    