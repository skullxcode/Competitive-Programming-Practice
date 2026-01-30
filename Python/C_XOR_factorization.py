import sys
input = lambda: sys.stdin.readline().rstrip()

def search(arr, target):
    arr.sort()
    l = 0
    r = len(arr) - 1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            r = mid - 1
        else:
            l = mid + 1
    return -1

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b):
    return ((a * b) // gcd(a, b))

def ceil(a, b):
    return (a + b - 1) // b

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def solve():
    # n = int(input())
    # a, b = map(int, input().split())
    # l = list(map(int, input().split()))
    
    
    pass

if __name__ == "__main__":
    try:
        t = int(input())
        for _ in range(t):
            solve()
    except ValueError:
        t = 1
        for _ in range(t):
            solve()
        pass