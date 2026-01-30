n = int(input())
t = False
if n%4==0 or n%7==0 or n%44==0 or n%47==0 or n%74==0 or n%77==0 or n%444==0 or n%447==0 or n%474==0 or n%477==0 or n%744==0 or n%747==0 or n%774==0 or n%777==0:
    print("YES")
else:
    print("NO")
# else:
#     while n>0:
#         if n%10==4 or n%10==7:
#             n//=10
#             t = True
#         else:
#             print('NO')
#             break
# if t == True:
#     print("YES")