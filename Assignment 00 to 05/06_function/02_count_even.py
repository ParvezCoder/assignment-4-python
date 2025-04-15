def count_even():
    listt = []
    count = 0
    get_value = input("Enter Even or Odd Number: ")
    # list.append(int(get_value))
    while get_value != "":
        listt.append(get_value)
        num = int(get_value)
        if num % 2 ==0:
            count +=1
        get_value = input("Enter Even or Odd Number::: ")
    print(count)
    print(listt)
    return list
count_even()
