def double():
    get_number = int(input("Enter a number which is less than 100: "))

    while get_number < 100 :
        print(get_number * 2)
        get_number = get_number * 2


double()