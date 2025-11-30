def getComposite(num):

    i = 1;
    count = 0;
    while( i <= num):
        if(num % i == 0):
            count+=1;
        i+=1;

    if(count > 2):
        return "Composite Number";
    else:
        return "Not a Composite Number"

    
num = int(input("Enter num: "));

print(getComposite(num));