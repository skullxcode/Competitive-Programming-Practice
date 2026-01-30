t = int(input())
for _ in range(t):
    n = int(input())
    for i in range(n):
        print(n-i, end=" ")
    print(n,end=" ")
    for j in range(1,n):
        print(j,end=" ")
    print()





# t = int(input())
# for _ in range(t):
#     n = int(input())
#     a = [x for x in range(1,n+1)]
#     for i in range(1,n):
#         for j in range(n):
#             if ((n+i)-a[j])%a[j]==0:
#                 a.append(j)
#                 break
#             else:
#                 continue
#     print(a)
            
        
        
        
        
        
        
    #     for j in range(i,0):
    #         if (n+j-i)%i==0:
    #             a.append(i)
    #             break
    #         else:
    #             continue
    # print(a)