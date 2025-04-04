lst = []  

def print_list(): 
    list_element = input("\033[94m Enter a value \033[0m ")  # Blue text
    while list_element != "":
        lst.append(list_element)
        list_element = input("\033[94m Enter a value \033[0m ")  # Blue text
    return lst

print_list()
print("Here is the list:", lst)
 