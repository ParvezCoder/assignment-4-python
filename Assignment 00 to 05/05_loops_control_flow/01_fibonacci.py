max_num = 10000
def fahb():
    num1 = 0
    num2 = 1
    while num1 <= max_num:
        print(num1)
        tem = num1
        num1 = num2
        num2 = num2 + tem

fahb()