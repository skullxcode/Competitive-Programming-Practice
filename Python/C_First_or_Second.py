t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    
    dp = [0]*n
    
    for j in range(n-1,0,-1):
        dp1 = [0]*n
        for i in range(j):
            if j == n-1:
                dp1[i]= max(a[i],-a[j])
            else:
                dp1[i]= max(a[i]+dp[j], -a[j]+dp[i])
        dp = dp1
    print(dp[0])
    
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     a = list(map(int, input().split()))
#     dp = [0]*n
#     for j in range(n-1, 0, -1):
#         new_dp = [0]*n
#         for i in range(j):
#             if j == n-1:
#                 new_dp[i] = max(a[i], -a[j])
#             else:
#                 new_dp[i] = max(
#                     a[i] + dp[j],
#                     -a[j] + dp[i]
#                 )
#         dp = new_dp

#     print(dp[0])
