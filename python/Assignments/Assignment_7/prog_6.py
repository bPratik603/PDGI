data = input("Enter single value: ");

if(len(data) > 1):
    print("Enter Single value");
else:
    if(ord(data) >= 65 and ord(data) <= 90):
        print("Uppercase Letter");
    elif(ord(data) >= 97 and ord(data) <= 122):
        print("Lowercase Letter");
    elif(ord(data) >= 47 and ord(data) <= 57):
        print("Digit");
    else:
        print("Special Character"); 