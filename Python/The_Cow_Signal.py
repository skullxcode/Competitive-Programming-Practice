with open("cowsignal.in", "r") as fin:
    M, N, K = map(int, fin.readline().split())
    
    grid = [list(fin.readline().strip()) for _ in range(M)]

with open("cowsignal.out", "w") as fout:
    for i in range(M):
        for k in range(K):
            for j in range(N):
                fout.write(grid[i][j] * K)
            fout.write('\n')