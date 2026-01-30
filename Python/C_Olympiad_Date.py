# t = int(input())
# for _ in range(t):
#     n = int(input())
#     a = list(map(int, input().split()))
#     k = len(a)
#     l = False
#     zero = 0
#     one = 0
#     two = 0
#     three = 0
#     five = 0
#     m = 0
#     for i in range(k):
#         if zero >= 3 and one >= 1 and two >= 2 and three >= 1 and five >= 1:
#             m = i
#             break
#         if a[i]==0:
#             zero+=1
#         elif a[i]==1:
#             one+=1
#         elif a[i]==2:
#             two+=1
#         elif a[i]==3:
#             three+=1
#         elif a[i]==5:
#             five+=1
#         else:
#             l = True
#     if zero >= 3 and one >= 1 and two >= 2 and three >= 1 and five >= 1:
#         if m == n-1:
#             print(n-1)
#         else:
#             print(i+1)
#     else:
#         print(0)

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    zero = one = two = three = five = 0
    ans = 0
    
    for i in range(n):
        zero += (a[i] == 0)
        one  += (a[i] == 1)
        two  += (a[i] == 2)
        three+= (a[i] == 3)
        five += (a[i] == 5)

        if zero >= 3 and one >= 1 and two >= 2 and three >= 1 and five >= 1:
            ans = i + 1  
            break
    
    print(ans)