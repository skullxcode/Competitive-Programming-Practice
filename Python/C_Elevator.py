door = input().strip()
rail = int(input().strip())
if (door == "front" and rail == 1) or (door == "back" and rail == 2):
    print("L")
else:
    print("R")