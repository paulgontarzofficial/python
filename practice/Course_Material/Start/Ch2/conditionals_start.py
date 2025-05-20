# LinkedIn Learning Python course by Joe Marini
# Example file for working with conditional statements


x, y = 100, 100

# conditional flow uses if, elif, else

if x < y: 
    print("x is less than y")
elif x == y:
    print("x is the same as y")
else:
    print("y is less than x")

# conditional statements let you use "a if C else b"

result = "x is less than y" if (x < y) else "x is greater than y"
print(result)