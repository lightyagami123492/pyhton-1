units = int(input("please enter the number of units:"))

amount = 0 
surcharge = 0

if units <= 50:
    amount = units * 2.60
    surcharge = 25 

elif units <= 100:
    amount = 130 + ((units - 50)* 3.25)
    surcharge = 35

elif units <= 200:
    amount = 130 + (50 * 3.25) + ((units - 100) * 5.26)
    surcharge = 45

else:
    amount = 130 + 16.50 + 526 + ((units - 200)) * 8.45
total = amount + surcharge
print("\nEletricity bill = %.2f" % total)