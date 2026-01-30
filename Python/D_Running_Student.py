n,vb,vs= map(int,input().split())
stops = list(map(int,input().split()))
x,y = map(int,input().split())
y = y**2
times = []
stops = stops[1::]
ans = 1
dist = []
min_dist = 10**18
min_time = 10**18
for i in stops:
    total_dist = (abs(x-i)**2 + y)**0.5
    ts = total_dist/vs
    tb = i/vb
    total_time = ts+tb
    if(total_time < min_time) :
        min_time = total_time
        min_dist = total_dist
    elif total_time == min_time :
        min_dist = min(min_dist, total_dist)

ans_li = [i for i,x in enumerate(times) if x == min_time]
li1 = []
for i in ans_li:
    li1.append(dist[i])
an = min(li1)
ans = dist.index(an)
print(ans+2)

