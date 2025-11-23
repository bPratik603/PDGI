k = 1;

for i in range(6):
    for j in range(3):
        if(k == 1):
            print("#",end="");
        elif(k == 2):
            print("$",end="");
        elif(k == 3):
            print("@",end="");
    print();
    k +=1;
    if( k == 4):
       k = 1;
