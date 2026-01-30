n = int(input())
l = 0
r = n
ans = (l+r)/2
while l<=r:
    mid = (l+r)/2
    if mid*mid==n:
        ans = mid
        break
    elif mid*mid<=n:
        l = mid + 0.000000000001
        if abs(n-(ans*ans))>abs(n-(mid*mid)):
            ans = mid
    else:
        r = mid - 0.000000000001
print(ans)