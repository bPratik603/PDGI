def checkVoteEligibility(age):
 
    if(age > 18):
        print("Person Eligible for voting");
    else:
        print("Person Not Eligible for voting");


age = int(input("Enter age: "));
checkVoteEligibility(age);