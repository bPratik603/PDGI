def checkChar(char):
    
    if(len(char) > 1):
        print("Please Enter Single Charactor");
        return;

    if(char == 'a' or char == 'A' or char == 'e' or char == 'E' or char == 'i' or char == 'I' or char == 'o' or char == 'O' or char == 'u' or char == 'U'):
        print(char," is vowel");
    else:
        print(char," is consonant");


char = input("Enter character: ");
checkChar(char);