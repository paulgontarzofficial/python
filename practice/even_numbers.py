# for x in range(0,10,2):
#     x = 0
#     if x % 2 == 0:
#         print(x)
#         x += 1
#     else:
#          continue
# print("We have",x,"even numbers" )

counter = 0

for x in range(10):
    if x > 0:
        if x % 2 == 0:    
            print(x)
            counter +=1

print("We have",counter,"even numbers")