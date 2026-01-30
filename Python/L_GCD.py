a,b = map(int,input().split())
while b>0:
    c = a
    a = b
    if c%b==0:
        break
    b = c%b
print(b)


def findGCD(a, b):
    if a == 0:
        return b
    print(b % a, a)
    return findGCD(b % a, a)

# Main function
def main():
    a, b = map(int,input().split())
    g = findGCD(a, b)
    print(g)

if __name__ == "__main__":
    main()