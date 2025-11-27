angle1 = int(input("Enter angle 1: "));
angle2 = int(input("Enter angle 2: "));
angle3 = int(input("Enter angle 3: "));

if((angle1 < 90 and angle2 < 90 and angle3 < 90) and (angle1 + angle2 + angle3) == 180):
    print("Triangle is Acute");
elif((angle1 > 90 or angle2 > 90 or angle3 > 90) and (angle1 + angle2 + angle3) == 180):
    print("Triangle is Obtus");
elif (angle1 + angle2 + angle3) > 180:
    print("Invalid Triangle")