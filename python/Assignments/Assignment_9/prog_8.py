def getPrime(num):

     i = 1;
     count = 0;
     while(i <= num):

         if(num % i == 0 ):
             count+=1;
         i = i+1;

     return  "Prime Number" if count == 2 else "Not a Prime Number";


num = int(input("Enter num: "));

print(getPrime(num));