with open("speeding.in", "r") as fin:
    n,m = map(int,fin.readline().split())

    a = []
    for i in range(n):
        li = list(map(int,fin.readline().split()))
        a.append(li)
    b = []
    for i in range(m):
        li = list(map(int,fin.readline().split()))
        b.append(li)

with open("speeding.out", "w") as fout:
    ans = [0]
    i = 0
    j = 0
    while i<n and j<m:
        if a[i][1]<b[j][1]:
            ans.append(b[j][1]-a[i][1])
        if a[i][0]>b[j][0]:
            a[i][0]-=b[j][0]
            j+=1
            continue
        elif a[i][0]==b[j][0]:
            i+=1
            j+=1
            continue
        else:
            b[j][0]-=a[i][0]
            i+=1
            continue
    res = str(max(ans))
    fout.write(res)


# # with open("speeding.in", "r") as fin:
# n,m = map(int,input().split())

# a = []
# for i in range(n):
#     li = list(map(int,input().split()))
#     a.append(li)
# b = []
# for i in range(m):
#     li = list(map(int,input().split()))
#     b.append(li)

# # with open("speeding.out", "w") as fout:
# ans = [0]
# i = 0
# j = 0
# while i<n and j<m:
#     if a[i][1]<b[j][1]:
#         ans.append(b[j][1]-a[i][1])
#     if a[i][0]>b[j][0]:
#         a[i][0]-=b[j][0]
#         j+=1
#         continue
#     elif a[i][0]==b[j][0]:
#         i+=1
#         j+=1
#         continue
#     else:
#         b[j][0]-=a[i][0]
#         i+=1
#         continue
# res = str(max(ans))
# print(res)
# # fout.write(res)