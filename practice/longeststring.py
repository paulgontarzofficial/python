# def find_largest():
#     test_strings = [
#     "Hello World!",
#     "And how can this be? For he is the Kwisatz Haderach!",
#     "Four score and seven years ago",
#     "Life moves pretty fast. If you don’t stop and look around once in a while, you could miss it."
#     ]
    
#     # print(len(test_strings))

#     for i in test_strings[::]:
#         long_list = max(test_strings, key=len)
#         greatest_length = len(long_list)
#         return print(greatest_length)
        

#         #return max(len(i))
    
#     # print(len(test_strings[::]))
    
#     # for i in len(test_strings): 
#     #     print(test_strings[i])

# find_largest()


def find_largest(test_strings):
    for i in test_strings[::]:
        long_list = max(test_strings, key=len)
        greatest_length = len(long_list)
        return print(greatest_length)
    
find_largest(["Hello World!",
    "And how can this be? For he is the Kwisatz Haderach!",
    "Four score and seven years ago",
    "Life moves pretty fast. If you don’t stop and look around once in a while, you could miss it."])    