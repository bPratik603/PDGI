def fun(**data2,*data):
    print(data);
    print(type(data));
    
    for i,j in data.items():
        print(i," : ",j);


fun(name = "Pratik",age = 2310,20,30);