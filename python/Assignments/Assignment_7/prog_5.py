temp = int(input("Enter temperature: "));


if(temp < 0):
    print("Freezing cold");
elif(temp >= 0 and temp <= 10):
    print("very cold");
elif(temp >= 11 and temp <= 20):
    print("cold");
elif(temp >= 21 and temp <= 30):
    print("warm");
elif(temp >= 31 and temp <= 40):
    print("Hot");
else:
    print("Extreme Heat");