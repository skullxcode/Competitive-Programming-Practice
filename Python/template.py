with open("shuffle.in", "r") as fin:
    n = int(fin.readline())
    a = list(map(int,fin.readline().split()))
    b = list(map(int,fin.readline().split()))


with open("shuffle.out", "w") as fout:
    fout.write(str(ans))