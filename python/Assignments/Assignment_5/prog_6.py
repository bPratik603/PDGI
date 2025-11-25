char = input("Enter Char : ");

if(len(char) > 1):
     print("Please enter single charactor");
else:
     if((ord(char) >= 65 and ord(char) <= 90) or (ord(char) >= 97 and ord(char) <= 122)):
        print(char," is alphabet");

