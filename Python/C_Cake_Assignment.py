t = int(input())
for _ in range(t):
    k,x = map(int,input().split())
    a = x
    b = (2 ** (k+1)) - x
    final = 2 ** k
    operation = ""
    if a == final:
        print(0)
        print()
        continue
    while not a == final:
        if b >= a:
            operation += "1 "
            a_old = a
            a = 2 * a
            b = b - a_old
        else:
            operation += "2 "
            b_old = b
            b = 2 * b_old
            a = a - b_old
    move = operation.strip().split()
    result = ""
    i = len(move) - 1
    while i >= 0:
        result += move[i] + " "
        i = i - 1
    print(len(move))
    print(result.strip())