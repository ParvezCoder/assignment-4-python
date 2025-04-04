


def get_lst():
    lst = []
    list_elem: str = input("Please enter an element of the list or press enter to stop. ")
    while list_elem != "":
        lst.append(list_elem)
        list_elem = input("Please enter an element of the list or press enter to stop..... ")
    return lst

lst = get_lst()
print(lst[0])



