mecdical_cause = input("did you have a medical cause (Y/N): ").upper()

atten = int(input("Enter the attendence percentage of the student: "))

if mecdical_cause == "Y":
    print("you are allowed")
else:
    if atten >= 75:
        print("allowed")
    else:
        print("not allowed")