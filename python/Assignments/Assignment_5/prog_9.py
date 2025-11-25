char = input("Enter Char: ");


if(len(char) > 1):
   print("Enter single character");
else:
   if(char == 'a' or char == 'A' or char == 'e' or char == 'E' or char == 'i' or char == 'I' or char == 'o' or char == 'O' or char == 'u' or char == 'U'):
       print(char," is vowel");
   else:
       print(char," is consonant");

