x = 10;

def fun():
     nonlocal x;
     x = 11;
    
     print(x);

     def gun():
         #nonocal x;

         x = x+1;
         print("In gun: x ",x);

     return gun;
retGun = fun();
retGun();