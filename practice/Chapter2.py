# def count_numbers(which, numbers): 
#     numbers = [7, 17, 2, 13, 19, 20, 0, 5, 11, 1280, 105]
#     if which == "even":
#         numbers = numbers % 2
#     print(numbers)  

# count_numbers("even",(2, 5, 20, 30, 55))  

def count_numbers(which, nums):
    if which != "even" and which != "odd":
        return -1

    result = 0
    for num in nums: 
        if which == "even" and num % 2 == 0:
            result += 1
        if which == "odd" and num % 2 != 0:
            result += 1
    return result     