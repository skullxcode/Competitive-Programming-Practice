with open("shuffle.in", "r") as fin:
    n = int(fin.readline())
    a = list(map(int,fin.readline().split()))
    b = list(map(int,fin.readline().split()))


with open("shuffle.out", "w") as fout:
    l1 = []
    l2 = []
    l3 = []
    for i in a:
        l1.append(b[i-1])
    for i in a:
        l2.append(l1[i-1])
    for i in a:
        l3.append(l2[i-1])
    for i in l3:
        fout.write(str(i))
        fout.write("\n")
    
    
# n = int(input())
# a = list(map(int,input().split()))
# b = list(map(int,input().split()))   

# l1 = []
# l2 = []
# l3 = []
# for i in a:
#     l1.append(b[i-1])
# for i in a:
#     l2.append(l1[i-1])
# for i in a:
#     l3.append(l2[i-1])
# for i in l3:
#     print(str(i),)