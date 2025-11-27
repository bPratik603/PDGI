num = int(input("Ente num: "));


if(num > 0 and num %2 == 0):
    print("Positive Even");
elif(num > 0 and num % 2 == 1):
    print("Positive Odd");
elif(num < 0 and num % 2 == 0):
    print("Negative Even");
elif(num < 0 and num % 2 == 1):
    print("Negative Odd");
else:
    print("Zero");