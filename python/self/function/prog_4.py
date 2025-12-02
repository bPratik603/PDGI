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

        return run;
    return gun;

retGun = fun();
retRun = retGun();
retRun();

print(retGun.__closure__);
print(retRun.__closure__);
