# LinkedIn Learning Python course by Joe Marini
# Example file for using built-in functions
#

mystring = "The quick, brown fox jumped over the lazy dog!"
mynumbers = [1,3,5,6,9,12,14,17,20,30]

# the len() function calculates the length of a sequence

# print(len(mystring))
# print(len(mynumbers))

# the max() and min() functions will find the largest and smallest value in a sequence

print(min(mystring))
print(max(mynumbers))

# the str() function will return a string version of an object
prefix = "result: "
result = 5

# print(prefix + str(result))
# print(prefix + str(3.14159))
# print(prefix + str(4 + 2))

# for i in range(5, 15):
#     print(i)

# for i in range(5, 15, 2):
#     print(i)

for i in range(2, len(mystring), 2):
    print(mystring[i])


for i in range(2, len(mystring), 2):
    print(i)


# range(start, stop, step) will create a range of numbers 
# You can use ranges along with loops 



# the print function itself is pretty flexible - you can embed variables directly in it
greeting = "Hello!"
count = 10

print(f"{greeting} you are visitor number {count}")


# Using the bin() function to translate an integer to a binary string. 
print(bin(4572348))

