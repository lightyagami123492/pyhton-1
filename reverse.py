string = input("please enter your own string:")

string2= ('')

for i in string:
    if i in string:
        string2 = i + string2

print("\nThe oriiginal string is :", string)
print("the reversed string is = ", string2)