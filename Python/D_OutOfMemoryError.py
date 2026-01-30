# Soln 1


t = int(input())
for _ in range(t):
    n,m,h = map(int,input().split())
    arr = list(map(int,input().split()))
    sol = arr[:]
    l = [-1]*n
    time = 0
    rest = 0

    for i in range(m):
        b,c = map(int,input().split())
        b-=1
        time+=1
        if l[b]<rest:
            curv = arr[b]
        else:
            curv = sol[b]
        curv+=c
        if curv>h:
            rest = time
        else:
            sol[b] = curv
            l[b] = time
    ans = []
    for i in range(n):
        if l[i]<rest:
            ans.append(arr[i])
        else:
            ans.append(sol[i])
    print(*ans)

# # Wrong Soln 2

# t = int(input())
# for _ in range(t):
#     n,m,h = map(int,input().split())
#     arr = list(map(int,input().split()))
#     check = arr[:]
#     li = []
#     last = -1
#     for i in range(m):
#         l1 = list(map(int,input().split()))
#         li.append(l1)
#     for i in range(m):
#         indx = li[i][0]-1
#         val = li[i][1]
#         if check[indx]+val>h:
#             last = i
#         else:
#             check[indx]+=val
#     for j in range(last+1,m):
#         arr[li[j][0]-1] += li[j][1]
#     print(*arr)