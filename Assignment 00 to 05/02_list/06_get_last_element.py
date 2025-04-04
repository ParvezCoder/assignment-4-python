
def get_last_element():
    element = []
    take_element = input("enter element for adding in list. And press enter for stop")
    while take_element != "":
        element.append(take_element)
        take_element = input("enter element for adding in list. And press enter for stop")
    return element

element = get_last_element()

print(element[-1])