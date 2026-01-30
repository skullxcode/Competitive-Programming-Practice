n = int(input())

for i in range(n + 1):
    print("  " * (n - i), end="")
    
    for j in range(i):
        print(j, end=" ")
    
    print(i, end="")
    for j in range(i - 1, -1, -1):
        print(" " + str(j), end="")
    print()

for i in range(n - 1, -1, -1):
    print("  " * (n - i), end="")
    
    for j in range(i):
        print(j, end=" ")
    
    print(i, end="")
    for j in range(i - 1, -1, -1):
        print(" " + str(j), end="")
    
    print()
