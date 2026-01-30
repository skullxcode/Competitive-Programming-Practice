n,k = map(int, input().split())
for i in range(n+1):
    if (i*(i+1)/2) - (n-i) == k:
        print(n-i)
        break


# n, k = map(int, input().split())
# limit = int((2*(n+k))**0.5) + 2
# for i in range(limit):
#     if (i*(i+1)//2) - (n-i) == k:
#         print(n - i)
#         break
