p = False
while p == False:
    password = int(input())
    if password == 1999:
        print("Correct")
        p == True
        break
    else:
        print("Wrong")
        p == False