n = int(input())
n = n%1000000007
def pell(n):
    n%=1000000007
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        return (2*pell((n-1))+pell(n-2))%1000000007
print(pell(n))