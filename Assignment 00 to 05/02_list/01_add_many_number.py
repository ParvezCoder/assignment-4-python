def add_many_number(number):
    total_sum = 0
    for add in number:
        total_sum += add
    return total_sum


numbers = [2,4,6,8,8]
result = add_many_number(numbers)
print("The Total of All number is ",result)
