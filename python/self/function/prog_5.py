def fun():
    x = 10;

    print("In fun x : ",x);

    def gun():
        nonlocal x;
        x = x+1;
        print("In gun x : ",x);

    def run():
            nonlocal x;
            x = x+1;
            print("In run x : ",x);

        
    return gun,run;

retFn = fun();

for Fn in retFn:
    Fn();
    print(Fn.__closure__[0].cell_contents);
    print(type(Fn.__closure__[0]));
