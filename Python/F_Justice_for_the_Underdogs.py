PI = 3.14159265358979323846
E = 2.718281828459045
INF = 1000000000000000000
MOD1 = 1000000007
MOD2 = 998244353
 
def solve(fact):
    # n = int(input())
    n , k = list(map(int, input().split()))
    # print(n-k)
    mod = 998244353
    def power(a,b,mod):
        if b == 1:
            return a % mod
        if b%2 == 0:
            return (power(a,b//2,mod)**2)%mod
        else:
            return ((a % mod) * ((power(a,b//2,mod)**2) % mod)) % mod
    a = ((fact[n+1] % mod) * (power(fact[k+1],mod-2,mod) % mod)) % mod
    b = (a * (power(fact[n-k],mod-2,mod) % mod)) % mod
    print(b)
 
    # print(int(fact[n+1]/(fact[k+1] * fact[n-k])))
 
 
def main():
    mod = 998244353
    fact = [1,1]
    for i in range(2,(10**6)+2):
        fact.append((fact[-1]*i)%mod)
    t = 1
    t = int(input()) 
    for _ in range(t):
        solve(fact)
 
main()