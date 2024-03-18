def calculate_lcm(x, y):  
    greater = x if x > y else y  
    while(True):  
        if((greater % x == 0) and (greater % y == 0)):  
            break  
        greater += 1  
    print(greater)


calculate_lcm(4,6)