def looping():
    num = int(input('Please enter a number from 1-100: '))
    while num < 100:
    
        if num % 2 == 0:
            print(f'{num} is an even number')
            break  
        elif num % 2 == 1: 
            print(f'{num} is an odd number')
            break       
    else: 
        print('Please enter a number less than 100')
        looping()

looping()            