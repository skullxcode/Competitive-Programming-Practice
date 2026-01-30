def binary_search(arr,target):
    arr.sort()
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left+right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1

my_target = int(input())
my_arr = list(map(int,input().split()))
result = binary_search(my_arr,my_target)
if result != -1:
    print(f"Position of target value is {result+1}")
else:
    print("Value not found in given Array!")