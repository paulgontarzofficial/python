# def capitals(x):
#     caps = ["ABCDEFGHIKJKLMNOPQRSTUVWXYZ"]
#     for caps in x:
#         print(x.isupper())

# capitals("FrNKy")

def capitals(word):

    x = []

    for char in word: 
        if char.isupper():  
            x.append(char)
    return x

print(capitals("AbCDeF"))