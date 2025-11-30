def getFact(num):

    fact = 1;
    while(num != 0):
        fact = fact * num;
        num-=1;

    return fact;


num = int(input("Enter num: "));

print("Factorial : ",getFact(num));