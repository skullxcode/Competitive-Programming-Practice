t = int(input())
for _ in range(t):
    n = int(input())
    bin_num = input()
    is_rem = False
    for i in range(n//2 + 1):
        num_first = bin_num[0:1]
        num_last = bin_num[n-1:n]
        if num_first != num_last:
            bin_num = bin_num[1:n-1]
            is_rem = True
        else:
            is_rem = False
            break
    if bin_num == "":
        print(0)
    elif is_rem == False:
        print(n)
    else:
        print(len(bin_num))