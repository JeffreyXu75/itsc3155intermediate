string = input("Enter a string: ")
newdict = {}
for i in string:
    if i.lower() in newdict:
        newdict[i.lower()]+=1
    else:
        newdict[i.lower()] =1
print(newdict)