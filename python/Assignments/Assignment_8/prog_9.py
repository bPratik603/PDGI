def avg(*args):

    iter = 0;
    sum = 0;
    while ( iter < len(args)):
        sum = sum + args[iter];
        iter = iter + 1;

    print("Average: ",sum/len(args));

avg(1,2,3,4,5);