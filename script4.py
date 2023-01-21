
x=0
i=1
while i < 6:
    user = input("Enter int #" + str(i) + ": ")
    if (user.startswith("-") and user[1:len(user)].isnumeric()) or user.isnumeric():
        x += int(user)
        i+=1
    else:
        print("Invalid input. Please enter an int.")
print("Your sum is "  + str(x))