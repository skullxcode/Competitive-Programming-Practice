#lucky number Checker
def isLucky(n):
    while n>0:
        if n%10 == 4 or n%10 == 7:
            n//=10
            lucky = True
        else:
            lucky = False
            break
    return lucky

#input
a,b = map(int,input().split())

#check if any in range is lucky
anyLucky = False

#func call
for i in range(a,b+1):
    if isLucky(i):
        print(i, end = " ")
        anyLucky = True

if anyLucky == False:
    print(-1)