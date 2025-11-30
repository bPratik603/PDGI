def getPerfectNum(num):

    i = 1;
    sum = 0;
    while(i < num):
        if(num % i == 0):
            sum = sum + i;
        i+=1;

    if(sum == num):
        return "Perfect Number";
    else:
        return "Not a Perfect Number";

num = int(input("Enter num: "));

print(getPerfectNum(num));