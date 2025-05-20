cars = ['Volkswagon','Honda','Toyota', 'Chevy' ]


## Accessing a list using a for loop.
for i in cars: 
    print(i)


## Printing a range starting at 0 and going to 50, stepping by 2
for i in range(0,50,2):
    print(i)

## Using a string, we can utilize a for loop to iterate over that string. Also, using builtin functions like .upper/.lower. 
for letter in 'Python':
    print(letter.upper())


## Nested for loops 

numbers = [[1,2], [3,4], [5,6]] 

for num in numbers: 
    for number in num: 
        print(number)  


numbers = [[1,2], [3,4], [5,6]] 

for num in numbers: 
    for number in num: 
        print(num)