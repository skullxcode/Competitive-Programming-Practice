def binary_search(arr,target):
    arr.sort()
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left+right) // 2
        if arr[mid] >= target:
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    return ans

my_target = int(input())
my_arr = list(map(int,input().split()))
result = binary_search(my_arr,my_target)
print(result)