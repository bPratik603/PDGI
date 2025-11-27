amount = int(input("Enter purchase amount: "));

if(amount < 1000):
    print("discount Applied: No Discount");
    print("Final Amount : ",amount);
elif(amount >= 1000 and amount <= 4999):
    print("discount Applied: 5%");
    print("Final Amount : ", amount - (amount * 0.05));
elif(amount >= 5000 and amount <= 9999):
    print("discount Applied: 10%");
    print("Final Amount : ", amount - (amount * 0.10));
elif(amount >= 10000 and amount <= 19999):
    print("Discount Applied: 20%");
    print("Final Amount : ", amount - (amount * 0.20));
else:
    print("Discount Applied: 30%");
    print("Final Amount : ", amount - (amount * 30));