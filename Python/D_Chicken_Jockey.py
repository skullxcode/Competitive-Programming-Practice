PI = 3.14159265358979323846
E = 2.718281828459045
INF = 1000000000000000000
MOD1 = 1000000007
MOD2 = 998244353
 
def solve():
    # n = int(input())
    a = list(map(int, input().split()))
 
    fr = {}
 
    for i in a:
        if i not in fr:
            fr[i] = 0
        fr[i] += 1
    
    ans = 1 
 
    # def fact(n):
    #     if n <= 1:
    #         return 1
        
    #     return n * fact(n-1)
    for i in fr:
        if fr[i] >= 2:
            ans += (fr[i]*(fr[i]-1))//2
    print(ans%998244353)
 
 
    
 
def main():
    t = 1
    t = int(input()) 
    for _ in range(1):
        solve()
 
main()