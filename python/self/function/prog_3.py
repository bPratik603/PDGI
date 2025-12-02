def fun():
    x  = 10;
    print("In fun x : ",x);

    def gun():
        nonlocal x;

        print("In gun x : ",x);

    return gun;

retGun = fun();
retGun();

print(retGun.__closure__);
print(retGun.__closure__[0].cell_contents);
    