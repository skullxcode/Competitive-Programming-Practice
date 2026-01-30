n = int(input())
a = list(map(int,input().split()))
max_sum = a[0]
max_indx = a[0]

for i in range(1,n):
    max_indx = max(max_indx+a[i],a[i])
    max_sum = max(max_sum,max_indx)

print(max_sum)