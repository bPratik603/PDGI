char = input("Enter char: ");

if(len(char) > 1):
    print("Enter single charactor");
else:
    if(ord(char) % 2 == 0):
        print("Even");
    else:
         print("Odd");