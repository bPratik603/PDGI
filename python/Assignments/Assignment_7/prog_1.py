age = int(input("Enter age: "));
weight = float(input("Enter weight: "));
Hb = float(input("Enter Hb: "));


if((age > 18 and age < 65) and (weight > 50) and (Hb > 13.4)):
    print("Eligible for blood donation");
else:
    print("Not eligible for blood donation");