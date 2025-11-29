def printASCII(char):
    
    if(len(char) > 1):
        print("Please enter single charactor");
        return;

    print(ord(char));


char = input("Enter Character: ");

printASCII(char);