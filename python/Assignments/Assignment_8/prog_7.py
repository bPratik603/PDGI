def checkMaxNum(num1,num2):
    
    if(num1 > num2):
        print(num1," is greater then ",num2);
    elif(num2 > num1):
        print(num2," is greater then ",num1);
    else:
        print("Both are equal");


num1 = int(input("Enter num1: "));
num2 = int(input("Enter num2: "));

checkMaxNum(num1,num2);