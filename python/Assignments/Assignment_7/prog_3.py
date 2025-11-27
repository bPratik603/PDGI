unit = int(input("Ente unit: "));

if(unit <= 100):
    print("Total Bill: ",unit * 5,"rs");
elif(unit >= 101 and unit <= 200):
    print("Total Bill: ",unit * 7,"rs");
elif(unit >= 201 and unit <= 300):
    print("Total Bill: ",unit * 10);
else:
    print("Total Bill: ",unit * 15);