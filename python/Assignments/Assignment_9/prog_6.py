def getProduct(num):

    prod = 1;
    iter = 1;
    while(iter <= num):
        prod = prod * iter;
        iter = iter +1;

    return prod;


num = int(input("Enter num : "));

print("Poduct: ",getProduct(num));

