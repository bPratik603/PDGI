def getAvg(subjectData):
    
    sum = 0;
    for subject in subjectData:
        sum = sum +subject;

    return sum / len(subjectData);


subjectData = [];

i = 1;
while( i <= 5):
    subjectData.append(int(input("Enter subject "+str(i)+" marks: ")));
    i +=1;

print("Average: ",getAvg(subjectData));