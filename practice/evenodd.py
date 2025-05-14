# Exercise 2:
# Ask the user for a number:

# If it’s even, print "That’s an even number!"

# If it’s odd, print "That’s an odd number!"

# (Hint: Use the modulus operator %)

def even_odd():
    number = int(input("Enter a number: "))
    if number % 2 == 0:
        print("That's an even number!")
    else:
        print("That's and odd number!")    

even_odd()
