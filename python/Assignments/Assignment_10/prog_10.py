retFn = lambda year:(
          print(year," is leap year") if(year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)) else
          print(year," is not leap year")
        )

year = int(input("Enter year: "));

retFn(year);