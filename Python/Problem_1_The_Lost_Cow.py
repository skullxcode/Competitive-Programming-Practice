with open("lostcow.in", "r") as fin:
    x,y = map(int,fin.readline().split())

with open("lostcow.out", "w") as fout:
    res = abs(y-x)
    if x>y:
        res = -res
    d = 0
    i = 0
    ans = 0
    k = 3
    si = 1
    if res>0:
        while d<res:
            d = si*(2**i)
            if si == 1:
                si=-1
            else:
                si = 1
                
            if i==0:
                ans+=1
            elif i==1:
                ans+=k
            else:
                k*=2
                ans+=k
            i+=1
    else:
        while d>res:
            d = si*(2**i)
            if si == 1:
                si=-1
            else:
                si = 1
                
            if i==0:
                ans+=1
            elif i==1:
                ans+=k
            else:
                k*=2
                ans+=k
            i+=1

    ans = str(abs(ans-abs(abs(d)-abs(res))))
    fout.write(ans)

# x,y = map(int,input().split())
# res = abs(y-x)
# if x>y:
#     res = -res
# d = 0
# i = 0
# ans = 0
# k = 3
# si = 1
# if res>0:
#     while d<res:
#         d = si*(2**i)
#         if si == 1:
#             si=-1
#         else:
#             si = 1
            
#         if i==0:
#             ans+=1
#         elif i==1:
#             ans+=k
#         else:
#             k*=2
#             ans+=k
#         i+=1
# else:
#     while d>res:
#         d = si*(2**i)
#         if si == 1:
#             si=-1
#         else:
#             si = 1
            
#         if i==0:
#             ans+=1
#         elif i==1:
#             ans+=k
#         else:
#             k*=2
#             ans+=k
#         i+=1

# ans = abs(ans-abs(abs(d)-abs(res)))
# print(ans)
