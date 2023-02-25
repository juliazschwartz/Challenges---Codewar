#Script simulating a cash register, returning the smartest change in BRAZILIAN REAL (R$), in coins and bills.
# for bills ONLY:
value = int(input('value: '))

value;

bills = [200,100,50,20,10,2,1]; #these are the existing values for the brazilian bills

while True:
    for i in bills:
        if value >= i:
            print('{} bill of {}'.format(value//i, i))
            value = value%i
            
        if value == 0:
            break


#for bills and coins:

value = float(input('value: '))
value
notes = [200,100,50,20,10,2,1]  #these are the existing values for the brazilian bills
coins = [0.50, 0.25, 0.10, 0.05, 0.01] #these are the existing values for the brazilian coins

while True:
    for i in notes:
        if value >= i:
            print('{} bill of {}'.format(int(value//i), i))
            value = value%i
        if value == 0:     
            break

    for B in coins:
            if (value / B) >= 2 :
            
                    print('{} COIN of {}'.format(round(value//B), B))
                    value = value%B
           
    
            if value == 0:     
                    break
