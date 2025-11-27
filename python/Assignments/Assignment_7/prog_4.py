income = int(input("Enter income: "))

if income <= 250000:
    print("No Tax")
elif income <= 500000:
    print("Tax to be paid:", income * 0.05)
elif income <= 1000000:
    print("Tax to be paid:", income * 0.20)
else:
    print("Tax to be paid:", income * 0.30)
