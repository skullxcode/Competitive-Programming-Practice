import sys

# --- USACO FILE I/O ---
# sys.stdin = open("problemname.in", "r")
# sys.stdout = open("problemname.out", "w")
# ----------------------

input = lambda: sys.stdin.readline().rstrip()

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, b % a)

def lcm(a, b):
    return ((a * b) // gcd(a, b))

def ceil(a, b):
    return (a + b - 1) // b

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

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

def solve():
    # n = int(input())
    # a, b = map(int, input().split())
    # l = list(map(int, input().split()))
    
    
    pass

if __name__ == "__main__":
    solve()