char1 = input("Enter char 1: ");
char2 = input("Enter char 2: ");

if((ord(char1) % 2 == 1) and (ord(char2) %2 == 1)):
    print(char1+char2);
else:
    print("No Output");