def getSum(num1,num2):
    
    sum = 0;
    while(num1 <= num2):
        sum = sum + num1;
        num1 = num1+1;

    return sum;


num1 = int(input("Enter start num : "));
num2 = int(input("Enter end num : "));

print("sum = ",getSum(num1,num2));