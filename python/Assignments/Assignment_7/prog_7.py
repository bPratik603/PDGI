percentage = int(input("Enter Percentage: "));
entScore = int(input("Enter Entrance Exam Score: "));

if(percentage >= 90 and entScore >= 90):
    print("Elite Program");
elif(percentage >= 80 and entScore >= 70):
    print("Standard Program");
elif(percentage >= 60 and entScore >= 50):
    print("Basic Program");
else:
    print("Not eigible");